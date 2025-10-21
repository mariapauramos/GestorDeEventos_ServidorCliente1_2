import tkinter as tk
from tkinter import ttk, messagebox
import requests

API_BASE = "http://localhost:8091/eventos"
ENDPOINT_LISTAR_EC = "/EC"

class GUIListarEC(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Listar Evento Cultural")
        self.geometry("900x500")
        self.configure(bg="white")
        self.resizable(False, False)
        self.crear_interfaz()

    def crear_interfaz(self):
        # Título
        tk.Label(self, text="🎭  Listar Evento Cultural", 
                 font=("Verdana", 16, "bold"), bg="white", fg="black").place(x=320, y=20)

        # Tabla
        columnas = ("IdEvento", "Nombre", "Ciudad", "Asistentes", "Fecha", "ValorEntrada", "TipoCultura", "ArtistaPrincipal")
        self.tabla = ttk.Treeview(self, columns=columnas, show="headings", height=15)
        self.tabla.place(x=20, y=80, width=860, height=340)

        # Encabezados y columnas
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=100, anchor="center")

        # Scrollbar vertical
        scrollbar_y = ttk.Scrollbar(self, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar_y.set)
        scrollbar_y.place(x=880, y=80, height=340)

        # Botones
        tk.Button(self, text="Listar", font=("Verdana", 11, "bold"), command=self.listar_eventos).place(x=300, y=440, width=120)
        tk.Button(self, text="Cerrar", font=("Verdana", 11, "bold"), command=self.destroy).place(x=460, y=440, width=120)

    def listar_eventos(self):
        try:
            auth = ("admin", "admin")  # ✅ Autenticación básica del backend
            headers = {"Accept": "application/json"}

            resp = requests.get(API_BASE + ENDPOINT_LISTAR_EC, auth=auth, headers=headers)

            # Validar credenciales inválidas
            if resp.status_code == 401:
                messagebox.showerror("Acceso denegado", "No autorizado. Verifica usuario y contraseña (admin/admin).")
                return

            if resp.status_code == 200:
                eventos = resp.json()

                # Limpiar tabla antes de insertar
                for item in self.tabla.get_children():
                    self.tabla.delete(item)

                # Insertar solo eventos culturales (evita mezclar deportivos)
                for e in eventos:
                    if "tipoCultura" in e:  # ✅ Filtro para solo culturales
                        self.tabla.insert("", "end", values=(
                            e.get("idEvento", ""),
                            e.get("nombre", ""),
                            e.get("ciudad", ""),
                            e.get("asistentes", ""),
                            e.get("fecha", ""),
                            e.get("valorEntrada", ""),
                            e.get("tipoCultura", ""),
                            e.get("artistaPrincipal", "")
                        ))
            else:
                messagebox.showerror("Error",
                                    f"No se pudieron obtener los eventos. Código HTTP: {resp.status_code}")

        except Exception as e:
            messagebox.showerror("Error de conexión", f"No se pudo conectar al backend.\n{e}")
