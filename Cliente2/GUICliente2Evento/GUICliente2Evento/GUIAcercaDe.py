import tkinter as tk

class GUIAcercaDe(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Acerca de")
        self.geometry("500x400")
        self.configure(bg="white")
        self.resizable(False, False)


        # ====== Título ======
        tk.Label(
            self,
            text="ACERCA DE",
            font=("Verdana", 16, "bold"),
            bg="white",
            fg="black"
        ).place(x=200, y=50)

        # ====== Texto descriptivo ======
        descripcion = (
            "Desarrollado por:\n"
            "• Jonathan Moya, 2220222039\n"
            "• Mauricio Arturo Cañas, 2220211010\n\n"
            "• Maria Paula Ramos, 2220211032\n"
            "• Gileny Silva, 2220221010\n"
        )

        tk.Label(
            self,
            text=descripcion,
            justify="left",
            font=("Verdana", 13),
            bg="white",
            fg="black"
        ).place(x=50, y=130)

        # ====== Botón Cerrar ======
        tk.Button(
            self,
            text="Cerrar",
            font=("Verdana", 12, "bold", "italic"),
            bg="white",
            fg="blue",
            command=self.destroy
        ).place(x=200, y=340, width=100)