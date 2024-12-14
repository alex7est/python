from Laptop_Business import Laptop_Business
from tkinter import Tk, ttk, Text, StringVar, Canvas, NW
from PIL import Image, ImageTk
import random


class App:
    def __init__(self, root):
        self.root = root        
        self.laptops = []
        self.imagenes = [".\\img\\descarga (5).jpg", ".\\img\\descarga (6).jpg", ".\\img\\descarga (7).jpg", ".\\img\\descarga (8).jpg", ".\\img\\descarga (9).jpg"]

        root.title("Ingresar Datos de Laptop Empresarial")
        
        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self.root, text="Marca").grid(row=0, column=0)
        self.marca = StringVar()
        ttk.Entry(self.root, textvariable=self.marca).grid(row=0, column=1)

        ttk.Label(self.root, text="Procesador").grid(row=1, column=0)
        self.procesador = StringVar()
        ttk.Entry(self.root, textvariable=self.procesador).grid(row=1, column=1)

        ttk.Label(self.root, text="Memoria").grid(row=2, column=0)
        self.memoria = StringVar()
        ttk.Entry(self.root, textvariable=self.memoria).grid(row=2, column=1)

        ttk.Label(self.root, text="Almacenamiento").grid(row=3, column=0)
        self.almacenamiento = StringVar()
        ttk.Entry(self.root, textvariable=self.almacenamiento).grid(row=3, column=1)

        ttk.Label(self.root, text="Duración Batería (h)").grid(row=4, column=0)
        self.duracion_bateria = StringVar()
        ttk.Entry(self.root, textvariable=self.duracion_bateria).grid(row=4, column=1)
        
        ttk.Label(self.root, text="Precio").grid(row=5, column=0)
        self.costo = StringVar()
        ttk.Entry(self.root, textvariable=self.costo).grid(row=5, column=1)

        ttk.Button(self.root, text="Agregar Laptop", command=self.agregar_laptop).grid(row=6, column=0, columnspan=2)

        self.mostrar_laptops = Text(self.root, height=10, width=50)
        self.mostrar_laptops.grid(row=7, column=0, columnspan=2)

        self.canva = Canvas(self.root, width=200, height=200)
        self.canva.grid(row=0, column=2, rowspan=10)

    def agregar_laptop(self):
        nueva_laptop = Laptop_Business(
            self.marca.get(),
            self.procesador.get(),
            self.memoria.get(),
            self.almacenamiento.get(),
            self.duracion_bateria.get(),
            self.costo.get()
        )
        self.laptops.append(nueva_laptop)
        self.mostrar_laptops.insert('end', f"{nueva_laptop}--------------------\n")

        self.mostrar_imagen_aleatoria()

    def mostrar_imagen_aleatoria(self):
        imagen_path = random.choice(self.imagenes)
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((200,200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(imagen)
        
        self.canva.create_image(0,0, anchor=NW, image=photo)
        self.canva.image = photo

root = Tk()
app = App(root)
root.mainloop()
