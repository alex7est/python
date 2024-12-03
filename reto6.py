class auto:
    def __init__(self, marca, modelo, año, kilometraje=0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje

    def mostrar_informacion(self):
        print(f"Marca: {self.marca} Modelo: {self.modelo} Año: {self.año}")
    
    def actualizar_kilometraje(self, nuevo_kilometraje):
        if nuevo_kilometraje > self.kilometraje:
            self.kilometraje = nuevo_kilometraje
        else:
            print("No se puede reducir el kilometraje")
    
    def realizar_viaje(self, kilometros):
        if kilometros > 0:
            self.kilometraje += kilometros
        else:
            print("La cantidad de kilometros debe ser positiva")

    def estado_auto(self):
            if self.kilometraje < 20000:
                print("Estoy como nuevo")
            elif 20000 <= self.kilometraje <= 100000:
                print("Ya estoy usado")
            else:
                print("¡Ya déjame descansar por favor!")

mi_auto = auto("Toyota", "Corolla", 2020, 0)

mi_auto.mostrar_informacion()
mi_auto.actualizar_kilometraje(15000)
print(f"Kilometraje actual: {mi_auto.kilometraje}")

mi_auto.realizar_viaje(8000)
print(f"Kilometraje actual: {mi_auto.kilometraje}")

mi_auto.estado_auto()
mi_auto.actualizar_kilometraje(20000)
mi_auto.realizar_viaje(-500)
