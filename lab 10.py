#caso de veterinaria 
# class Animal:
#     def _init_(self, nombre, edad, peso):
#         self.nombre = nombre
#         self.edad = edad
#         self.peso = peso

#     def mostrar_datos_medicos(self):
#         return f"Nombre: {self.nombre}, Edad: {self.edad}, Peso: {self.peso} kg"

# class Perro(Animal):
#     def _init_(self, nombre, edad, peso, raza, datos_medicos, dosis, ficha_medica):
#         super()._init_(nombre, edad, peso)
#         self.raza = raza
#         self.datos_medicos = datos_medicos
#         self.dosis = dosis
#         self.ficha_medica = ficha_medica

#     def calcular_dosis(self):
#         return f"Dosis recomendada: {self.dosis} mg según especie"

#     def generar_ficha_medica(self):
#         return f"Ficha Médica:\nNombre: {self.nombre}\nEdad: {self.edad}\nPeso: {self.peso} kg\nRaza: {self.raza}\nDatos Médicos: {self.datos_medicos}\nDosis: {self.dosis} mg"

# class Gato(Animal):
#     def _init_(self, nombre, edad, peso, datos_medicos, dosis, ficha_medica):
#         super()._init_(nombre, edad, peso)
#         self.datos_medicos = datos_medicos
#         self.dosis = dosis
#         self.ficha_medica = ficha_medica

#     def calcular_dosis(self):
#         return f"Dosis recomendada: {self.dosis} mg según especie"

#     def generar_ficha_medica(self):
#         return f"Ficha Médica:\nNombre: {self.nombre}\nEdad: {self.edad}\nPeso: {self.peso} kg\nDatos Médicos: {self.datos_medicos}\nDosis: {self.dosis} mg"

# class Ave(Animal):
#     def _init_(