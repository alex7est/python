from Laptop import Laptop
import random

class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, memoria, almacenamiento, duracion_bateria, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.almacenamiento = almacenamiento
        self.duracion_bateria = duracion_bateria
    
    def __str__(self):
        return (f"Marca: {self.marca}\nProcesador: {self.procesador}\nMemoria: {self.memoria}\nAlmacenamiento: {self.almacenamiento}\nDuracion batería: {self.duracion_bateria}\nPrecio: {self.costo}\nImpuesto: {self.impuesto}\n")

    def realizar_diagnostico_sistema(self):
        diagnostico_base = super().realizar_diagnostico_sistema()
        diagnostico_base["ALMACENAMIENTO"] = "OK" if self.almacenamiento >= 256 else "Aumentar almacenamiento"
        diagnostico_base["DURACIÓN DE BATERÍA"] = "OK" if self.duracion_bateria >= 4 else "Verificar batería"
        
        return diagnostico_base

    def verificar_conectividad_red(self):
        conectividad = {
            "Wi-Fi Disponible": random.choice([True, False]),
            "Acceso a Servidores Empresariales": random.choice([True, False]),
            "Latencia de Red Estable": random.choice([True, False])
        }
        return conectividad


laptop_empresarial = Laptop_Business(
    marca="Lenovo",
    procesador="i7",
    memoria=16,
    almacenamiento=512,
    duracion_bateria=8,
    costo=1000,
    impuesto=50
)

diagnostico = laptop_empresarial.realizar_diagnostico_sistema()
#print(f"Diagnóstico del sistema empresarial: {diagnostico}")

conectividad = laptop_empresarial.verificar_conectividad_red()
#print(f"Resultados de conectividad de red: {conectividad}")