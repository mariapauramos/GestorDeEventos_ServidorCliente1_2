import tkinter as tk
from tkinter import ttk, messagebox
import requests

API_BASE = "http://localhost:8091/eventos"
ENDPOINT_EC = "/filtroEC"

class GUIListarFiltroEC(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Filtrar Eventos Culturales")
        self.geometry("950x550")
        self.configure(bg="white")
        self.resizable(False, False)
        self.crear_interfaz()

    def crear_interfaz(self):
        # ===== Título =====
        tk.Label(self, text="🎭  Filtrar Evento Cultural",
                 font=("Verdana", 16, "bold"), bg="white").place(x=330, y=20)

        # ===== Campos de Filtro =====
        tk.Label(self, text="Tipo Cultura:", font=("Verdana", 11), bg="white").place(x=100, y=80)
        self.tipoCultura_entry = tk.Entry(self, font=("Verdana", 11))
        self.tipoCultura_entry.place(x=220, y=80, width=200)

        tk.Label(self, text="Artista Principal:", font=("Verdana", 11), bg="white").place(x=450, y=80)
        self.artista_entry = tk.Entry(self, font=("Verdana", 11))
        self.artista_entry.place(x=600, y=80, width=200)

        tk.Button(self, text="Filtrar", font=("Verdana", 11, "bold"),
                  bg="lightblue", command=self.filtrar_eventos).place(x=380, y=120, width=120)

        # ===== Tabla =====
        columnas = ("idEvento", "nombre", "ciudad", "asistentes", "fecha",
                    "valorEntrada", "tipoCultura", "artistaPrincipal")
        self.tabla = ttk.Treeview(self, columns=columnas, show="headings", height=15)
        self.tabla.place(x=20, y=170, width=900, height=320)

        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=110, anchor="center")

        scrollbar_y = ttk.Scrollbar(self, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar_y.set)
        scrollbar_y.place(x=920, y=170, height=320)

        tk.Button(self, text="Cerrar", font=("Verdana", 11), command=self.destroy).place(x=410, y=500, width=120)

    def filtrar_eventos(self):
        tipoCultura = self.tipoCultura_entry.get().strip()
        artista = self.artista_entry.get().strip()

        if not tipoCultura and not artista:
            messagebox.showwarning("Campos vacíos", "Ingrese al menos un filtro.")
            return

        try:
            params = {}
            if tipoCultura:
                params["tipoCultura"] = tipoCultura
            if artista:
                params["artistaPrincipal"] = artista

            resp = requests.get(API_BASE + "/filtroEC", params=params, auth=("admin", "admin"))

            if resp.status_code == 200:
                eventos = resp.json()

                for row in self.tabla.get_children():
                    self.tabla.delete(row)

                if not eventos:
                    messagebox.showinfo("Sin resultados", "No se encontraron eventos.")
                    return

                for e in eventos:
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
                messagebox.showerror("Error", f"No se pudo filtrar. Código: {resp.status_code}")

        except Exception as e:
            messagebox.showerror("Error de conexión", f"No se pudo conectar al servidor.\n{e}")
