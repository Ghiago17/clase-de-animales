class Animales:
    def __init__(self, nombre, num_patas, fecha_vacunas, propietarios):
        self.nombre = nombre
        self.num_patas = num_patas
        self.fecha_vacunas = fecha_vacunas
        self.propietarios = propietarios

    def imprimir_atributos(self):
        mensaje = f"El animal {self.nombre} tiene {self.num_patas} patas."
        mensaje += f" últimas vacuna fue {self.fecha_vacunas}."
        mensaje += f' Sus propietarios son: {", ".join(self.propietarios)}.'
        print(mensaje)

mi_mascota = Animales(nombre="polo", num_patas=4, fecha_vacunas="10/02/2024", propietarios=["Jay-Z", "Valencia"])
mi_mascota.imprimir_atributos()
