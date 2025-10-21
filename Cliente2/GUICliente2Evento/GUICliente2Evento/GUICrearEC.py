import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import requests
from datetime import datetime

API_BASE = "http://localhost:8091/eventos"
ENDPOINT_CREAR_EC = "/EC"  

class GUICrearEC(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Crear Evento Cultural")
        self.geometry("580x500")
        self.configure(bg="white")
        self.resizable(False, False)

        self.img = tk.PhotoImage(file="images/cultural.png") 
        tk.Label(self, image=self.img, bg="white").place(x=50, y=10, width=80, height=80)

        tk.Label(self, text="CREAR EVENTO CULTURAL", font=("Verdana", 18, "bold"), bg="white").place(x=150, y=35)
        self.crear_formulario()

    def crear_formulario(self):
        labels = ["ID Evento:", "Nombre:", "Ciudad:", "Asistentes:", "Fecha:", 
                "Valor Entrada:", "Tipo Cultura:", "Artista Principal:"]
        self.entries = {}

        for i, text in enumerate(labels):
            tk.Label(self, text=text, font=("Verdana", 11), bg="white").place(x=50, y=80 + i * 45)
            if text == "Fecha:":
                entry = DateEntry(self, width=18, font=("Verdana", 11), date_pattern="yyyy-mm-dd")
            else:
                entry = tk.Entry(self, font=("Verdana", 11))
            entry.place(x=200, y=80 + i * 45, width=280)
            self.entries[text] = entry

        tk.Button(self, text="Crear", font=("Verdana", 11, "bold"), command=self.crear_evento).place(x=150, y=440, width=100)
        tk.Button(self, text="Cerrar", font=("Verdana", 11, "bold"), command=self.destroy).place(x=330, y=440, width=100)

    def validar(self):
        try:
            # Todos los campos obligatorios
            if not all(self.entries[label].get().strip() for label in self.entries):
                raise ValueError("Todos los campos son obligatorios.")

            # Conversión de tipos correcta
            int(self.entries["Asistentes:"].get())
            float(self.entries["Valor Entrada:"].get())

            # Validar formato de fecha (pero no importa si es pasada o futura)
            datetime.strptime(self.entries["Fecha:"].get(), "%Y-%m-%d")

            return True
        except Exception as e:
            messagebox.showwarning("Validación", str(e))
            return False

    def crear_evento(self):
        if not self.validar():
            return

        payload = {
            "idEvento": self.entries["ID Evento:"].get(),
            "nombre": self.entries["Nombre:"].get(),
            "ciudad": self.entries["Ciudad:"].get(),
            "asistentes": int(self.entries["Asistentes:"].get()),
            "fecha": self.entries["Fecha:"].get(),
            "valorEntrada": float(self.entries["Valor Entrada:"].get()),
            "tipoCultura": self.entries["Tipo Cultura:"].get(),
            "artistaPrincipal": self.entries["Artista Principal:"].get()
        }

        try:
            # ✅ AGREGADO: AUTENTICACIÓN BASIC Y HEADERS
            auth = ("admin", "admin")
            headers = {"Content-Type": "application/json"}

            resp = requests.post(API_BASE + ENDPOINT_CREAR_EC, json=payload, auth=auth, headers=headers)

            if resp.status_code in (200, 201):
                messagebox.showinfo("Éxito", "Evento Cultural creado correctamente.")
                self.limpiar()
            else:
                messagebox.showerror("Error", f" Código: {resp.status_code}\n{resp.text}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo conectar al backend.\n\n{e}")

    def limpiar(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
