import tkinter as tk
from tkinter import messagebox
import requests

API_BASE = "http://localhost:8091/eventos"

class GUIBuscarEC(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Buscar Evento Cultural")
        self.geometry("580x500")
        self.configure(bg="white")
        self.resizable(False, False)

        # ==== Imagen ====
        try:
            self.img = tk.PhotoImage(file="images/cultural.png")
            tk.Label(self, image=self.img, bg="white").place(x=50, y=10, width=80, height=80)
        except:
            pass

        # ==== Título ====
        tk.Label(self, text="BUSCAR EVENTO CULTURAL",
                 font=("Verdana", 18, "bold"), bg="white").place(x=150, y=35)

        self.crear_formulario()

    def crear_formulario(self):
        tk.Label(self, text="ID Evento:", font=("Verdana", 11), bg="white").place(x=50, y=100)
        self.id_entry = tk.Entry(self, font=("Verdana", 11))
        self.id_entry.place(x=180, y=100, width=220)
        tk.Button(self, text="Buscar", font=("Verdana", 10, "bold"),
                  command=self.buscar_evento).place(x=420, y=100, width=90)

        labels = ["Nombre:", "Ciudad:", "Asistentes:", "Fecha:",
                  "Valor Entrada:", "Tipo Cultura:", "Artista Principal:"]
        self.entries = {}

        for i, text in enumerate(labels):
            tk.Label(self, text=text, font=("Verdana", 11), bg="white").place(x=50, y=160 + i * 40)
            entry = tk.Entry(self, font=("Verdana", 11))
            entry.place(x=180, y=160 + i * 40, width=330)
            entry.config(state="readonly")
            self.entries[text] = entry

        tk.Button(self, text="Cerrar", font=("Verdana", 11, "bold"),
                  command=self.destroy).place(x=250, y=460, width=100)

    def buscar_evento(self):
        idEvento = self.id_entry.get().strip()
        if not idEvento:
            messagebox.showwarning("Campo vacío", "Por favor ingresa un ID válido.")
            return

        try:
            auth = ("admin", "admin")  # Autenticación básica
            headers = {"Accept": "application/json"}

            url = f"{API_BASE}/{idEvento}"
            print("DEBUG: Consultando URL ->", url)

            resp = requests.get(url, auth=auth, headers=headers) 
            print("DEBUG: Respuesta HTTP ->", resp.status_code)  

            if resp.status_code == 401:
                messagebox.showerror("Acceso denegado", "Credenciales incorrectas (admin/admin).")
                return

            if resp.status_code == 200:
                data = resp.json()
                print("DEBUG: JSON recibido:", data) 

                # Validar si es evento cultural
                if "tipoCultura" not in data:
                    messagebox.showwarning(
                        "Tipo incorrecto",
                        f"El ID {idEvento} pertenece a un evento deportivo, no cultural."
                    )
                    self.limpiar_campos()
                    return

                self.llenar_campos(data)

            else:
                messagebox.showinfo("Sin resultados", f"No existe evento con ID: {idEvento}")
                self.limpiar_campos()

        except Exception as e:
            messagebox.showerror("Error de conexión", f"No se pudo conectar al backend.\n{e}")


    def llenar_campos(self, data):
        self.limpiar_campos()
        # Habilitar temporalmente para escribir
        for entry in self.entries.values():
            entry.config(state="normal")

        self.entries["Nombre:"].insert(0, data.get("nombre", ""))
        self.entries["Ciudad:"].insert(0, data.get("ciudad", ""))
        self.entries["Asistentes:"].insert(0, data.get("asistentes", ""))
        self.entries["Fecha:"].insert(0, data.get("fecha", ""))
        self.entries["Valor Entrada:"].insert(0, data.get("valorEntrada", ""))
        self.entries["Tipo Cultura:"].insert(0, data.get("tipoCultura", ""))
        self.entries["Artista Principal:"].insert(0, data.get("artistaPrincipal", ""))

    def limpiar_campos(self):
        for entry in self.entries.values():
            entry.config(state="normal")
            entry.delete(0, tk.END)
            entry.config(state="readonly")


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    GUIBuscarEC(root)
    root.mainloop()
