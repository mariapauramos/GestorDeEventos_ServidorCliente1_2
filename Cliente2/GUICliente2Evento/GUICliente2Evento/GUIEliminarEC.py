import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests

API_BASE = "http://localhost:8091/eventos"

class GUIEliminarEC(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Eliminar Evento Cultural")
        self.geometry("600x610")
        self.configure(bg="white")
        self.resizable(False, False)

        # ===== Imagen =====
        try:
            imagen = Image.open("images/cultural.png").resize((80, 80))
            self.logo = ImageTk.PhotoImage(imagen)
            tk.Label(self, image=self.logo, bg="white").place(x=50, y=10)
        except:
            print("⚠️ No se encontró la imagen.")

        # ===== Título =====
        tk.Label(self, text="Eliminar Evento Cultural",
                 font=("Verdana", 16, "bold"), bg="white").place(x=180, y=35)

        # ===== Campo ID =====
        tk.Label(self, text="ID Evento:", font=("Verdana", 11), bg="white").place(x=50, y=130)
        self.entry_id = tk.Entry(self, font=("Verdana", 11))
        self.entry_id.place(x=200, y=130, width=280)

        # ===== Botones =====
        tk.Button(self, text="Buscar", font=("Verdana", 10, "bold"),
                  bg="lightblue", command=self.buscar_evento).place(x=200, y=170, width=100)

        tk.Button(self, text="Cerrar", font=("Verdana", 10, "bold"),
                  bg="lightgray", command=self.destroy).place(x=330, y=170, width=100)

        # ===== Campos =====
        self.entries = {}
        labels = ["Nombre:", "Ciudad:", "Asistentes:", "Fecha:",
                  "Valor Entrada:", "Tipo Cultura:", "Artista Principal:"]
        for i, text in enumerate(labels):
            y = 230 + i * 50
            tk.Label(self, text=text, font=("Verdana", 11), bg="white").place(x=50, y=y)
            entry = tk.Entry(self, font=("Verdana", 11))
            entry.place(x=200, y=y, width=280)
            entry.config(state="readonly")
            self.entries[text] = entry

        tk.Button(self, text="Eliminar", font=("Verdana", 10, "bold"),
                  bg="lightgray", command=self.eliminar_evento).place(x=250, y=580, width=100)

    
    # ========= Buscar ==========
    def buscar_evento(self):
        id_evento = self.entry_id.get().strip()
        if not id_evento:
            messagebox.showwarning("Campo vacío", "Por favor ingresa un ID válido.")
            return

        try:
            resp = requests.get(f"{API_BASE}/{id_evento}", auth=("admin", "admin"))
            if resp.status_code == 200:
                data = resp.json()
                if "tipoCultura" not in data:
                    messagebox.showwarning("Error",
                                           "Este evento no es cultural, no se puede eliminar aquí.")
                    self.limpiar_campos()
                    return
                self.llenar_campos(data)
            else:
                messagebox.showinfo("Sin resultados", f"No existe evento con ID {id_evento}")
                self.limpiar_campos()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo conectar al servidor.\n{e}")

    # ===== Llenar Campos =====
    def llenar_campos(self, data):
        for key, entry in self.entries.items():
            entry.config(state="normal")
            entry.delete(0, tk.END)

        self.entries["Nombre:"].insert(0, data.get("nombre", ""))
        self.entries["Ciudad:"].insert(0, data.get("ciudad", ""))
        self.entries["Asistentes:"].insert(0, data.get("asistentes", ""))
        self.entries["Fecha:"].insert(0, data.get("fecha", ""))
        self.entries["Valor Entrada:"].insert(0, data.get("valorEntrada", ""))
        self.entries["Tipo Cultura:"].insert(0, data.get("tipoCultura", ""))
        self.entries["Artista Principal:"].insert(0, data.get("artistaPrincipal", ""))

        for entry in self.entries.values():
            entry.config(state="readonly")

    # ===== Limpiar Campos =====
    def limpiar_campos(self):
        for entry in self.entries.values():
            entry.config(state="normal")
            entry.delete(0, tk.END)
            entry.config(state="readonly")

    # ========= Eliminar ==========
    def eliminar_evento(self):
        id_evento = self.entry_id.get().strip()

        if not id_evento:
            messagebox.showwarning("Advertencia", "Ingrese un ID para eliminar.")
            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Seguro que desea eliminar el evento con ID {id_evento}?"
        )
        if not confirmar:
            return

        try:
            resp = requests.delete(f"{API_BASE}/{id_evento}", auth=("admin", "admin"))
            if resp.status_code in (200, 204):
                messagebox.showinfo("Éxito", "Evento eliminado correctamente.")
                self.entry_id.delete(0, tk.END)
                self.limpiar_campos()
            else:
                messagebox.showerror("Error", f"No se pudo eliminar el evento.\n{resp.text}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo conectar al servidor.\n{e}")
