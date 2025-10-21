import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import requests
from PIL import Image, ImageTk

API_BASE = "http://localhost:8091/eventos"
ENDPOINT_EC = "/EC"

class GUIActualizarEC(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Actualizar Evento Cultural")
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
        tk.Label(self, text="Actualizar Evento Cultural",
                 font=("Verdana", 16, "bold"), bg="white").place(x=180, y=35)

        # ===== Campo ID =====
        tk.Label(self, text="ID Evento:", font=("Verdana", 11), bg="white").place(x=50, y=130)
        self.id_entry = tk.Entry(self, font=("Verdana", 11))
        self.id_entry.place(x=200, y=130, width=280)

        # ===== Botones Buscar y Cerrar =====
        tk.Button(self, text="Buscar", font=("Verdana", 10, "bold"),
                  bg="lightblue", command=self.buscar_evento).place(x=200, y=170, width=100)
        tk.Button(self, text="Cerrar", font=("Verdana", 10, "bold"),
                  bg="lightgray", command=self.destroy).place(x=330, y=170, width=100)

        # ===== Campos =====
        labels = ["Nombre:", "Ciudad:", "Asistentes:", "Fecha:",
                  "Valor Entrada:", "Tipo Cultura:", "Artista Principal:"]
        self.entries = {}
        for i, text in enumerate(labels):
            y = 230 + i * 50
            tk.Label(self, text=text, font=("Verdana", 11), bg="white").place(x=50, y=y)

            if text == "Fecha:":
                entry = DateEntry(self, font=("Verdana", 11), date_pattern="yyyy-mm-dd")
            else:
                entry = tk.Entry(self, font=("Verdana", 11))

            entry.place(x=200, y=y, width=280)
            self.entries[text] = entry

        # ===== Botones finales =====
        tk.Button(self, text="Editar", font=("Verdana", 10, "bold"),
                  bg="yellow", command=lambda: self.habilitar_campos(True)).place(x=180, y=580, width=100)
        tk.Button(self, text="Guardar", font=("Verdana", 10, "bold"),
                  bg="lightgreen", command=self.actualizar_evento).place(x=320, y=580, width=100)

        self.habilitar_campos(False)

    # ===== Buscar Evento =====
    def buscar_evento(self):
        idEvento = self.id_entry.get().strip()
        if not idEvento:
            messagebox.showwarning("Campo vacío", "Por favor ingresa un ID válido.")
            return

        try:
            auth = ("admin", "admin")
            headers = {"Accept": "application/json"}
            url = f"{API_BASE}/{idEvento}"

            resp = requests.get(url, auth=auth, headers=headers)

            if resp.status_code == 200:
                data = resp.json()
                if "tipoCultura" not in data:
                    messagebox.showwarning("Tipo incorrecto", "Este ID no corresponde a un evento cultural.")
                    self.limpiar_campos()
                    return
                self.llenar_campos(data)
                self.habilitar_campos(False)
            elif resp.status_code == 401:
                messagebox.showerror("Acceso denegado", "Credenciales inválidas (admin/admin).")
            else:
                messagebox.showinfo("Sin resultados", f"No existe evento con ID: {idEvento}")
                self.limpiar_campos()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo conectar al servidor.\n{e}")

    # ===== Llenar Campos =====
    def llenar_campos(self, data):
        for label, entry in self.entries.items():
            entry.config(state="normal")
            entry.delete(0, tk.END)
        self.entries["Nombre:"].insert(0, data.get("nombre", ""))
        self.entries["Ciudad:"].insert(0, data.get("ciudad", ""))
        self.entries["Asistentes:"].insert(0, data.get("asistentes", ""))
        self.entries["Fecha:"].delete(0, tk.END)
        self.entries["Fecha:"].insert(0, data.get("fecha", ""))
        self.entries["Valor Entrada:"].insert(0, data.get("valorEntrada", ""))
        self.entries["Tipo Cultura:"].insert(0, data.get("tipoCultura", ""))
        self.entries["Artista Principal:"].insert(0, data.get("artistaPrincipal", ""))

    # ===== Bloquear/Desbloquear campos =====
    def habilitar_campos(self, habilitar):
        for entry in self.entries.values():
            entry.config(state="normal" if habilitar else "readonly")

    # ===== Limpiar Campos =====
    def limpiar_campos(self):
        for entry in self.entries.values():
            entry.config(state="normal")
            entry.delete(0, tk.END)
            entry.config(state="readonly")

    def actualizar_evento(self):
        idEvento = self.id_entry.get().strip()
        try:
            payload = {
                "idEvento": idEvento,
                "nombre": self.entries["Nombre:"].get(),
                "ciudad": self.entries["Ciudad:"].get(),
                "asistentes": int(self.entries["Asistentes:"].get()),
                "fecha": self.entries["Fecha:"].get(),
                "valorEntrada": float(self.entries["Valor Entrada:"].get()),
                "tipoCultura": self.entries["Tipo Cultura:"].get(),
                "artistaPrincipal": self.entries["Artista Principal:"].get()
            }
            auth = ("admin", "admin")
            resp = requests.put(f"{API_BASE}{ENDPOINT_EC}/{idEvento}", json=payload, auth=auth)

            if resp.status_code in (200, 204):
                messagebox.showinfo("Éxito ✅", "Evento cultural actualizado correctamente.")
                self.limpiar_campos()          # <<< Limpia campos
                self.id_entry.delete(0, tk.END) # <<< Limpia ID también
            else:
                messagebox.showerror("Error", f"No se pudo actualizar.\n{resp.text}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

