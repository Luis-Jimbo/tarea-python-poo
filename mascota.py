# Definición de la clase (Objeto del mundo real)
class Mascota:
    # 1. Atributos (Nombre, Especie, Edad)
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    # 2. Método: Hacer sonido
    def hacer_sonido(self):
        if self.especie.lower() == "perro":
            print(f"{self.nombre} dice: ¡Guau guau!")
        elif self.especie.lower() == "gato":
            print(f"{self.nombre} dice: ¡Miau miau!")
        else:
            print(f"{self.nombre} hace un sonido extraño.")

    # 3. Método: Cumplir años
    def cumplir_años(self):
        self.edad += 1
        print(f"¡{self.nombre} ha cumplido años! Ahora tiene {self.edad} años.")

# --- Creación de objetos ---

# Objeto 1
mi_perro = Mascota("Max", "Perro", 3)
print(f"Mascota 1: {mi_perro.nombre}, un {mi_perro.especie} de {mi_perro.edad} años.")
mi_perro.hacer_sonido()
mi_perro.cumplir_años()

print("-" * 30)

# Objeto 2
mi_gato = Mascota("Luna", "Gato", 2)
print(f"Mascota 2: {mi_gato.nombre}, una {mi_gato.especie} de {mi_gato.edad} años.")
mi_gato.hacer_sonido()