#ej 1
# class ExperimentoFisico:
#     def realizar_experimento(self):
#         raise NotImplementedError("Este método debe ser implementado en una subclase.")

# class CaidaLibre(ExperimentoFisico):
#     def _init_(self, altura, gravedad):
#         if altura < 0:
#             raise ValueError("La altura no puede ser negativa.")
#         if gravedad <= 0:
#             raise ValueError("La gravedad debe ser mayor que cero.")
#         self.altura = altura
#         self.gravedad = gravedad

#     def realizar_experimento(self):
#         tiempo_caida = (2 * self.altura / self.gravedad) ** 0.5  
#         return tiempo_caida

# try:
#     altura =int(input("Ingrese la altura en metros: "))
#     gravedad = int(input("Ingrese la gravedad: "))
#     experimento = CaidaLibre(altura, gravedad)
#     print(f"Tiempo de caída: {experimento.realizar_experimento():.2f} segundos")
# except ValueError as e:
#     print(f"Error: {e}")

#ej 2 
# import math

# class OperacionCientifica:
#     def calcular(self, valor1, valor2=None):
#         pass

# class RaizCuadrada(OperacionCientifica):
#     def calcular(self, valor):
#         if valor < 0:
#             raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
#         return math.sqrt(valor)

# class Potencia(OperacionCientifica):
#     def calcular(self, base, exponente):
#         return math.pow(base, exponente)

# class Logaritmo(OperacionCientifica):
#     def calcular(self, valor, base=math.e):
#         if valor <= 0:
#             raise ValueError("El logaritmo solo se puede calcular para valores positivos.")
#         return math.log(valor, base)

# class Factorial(OperacionCientifica):
#     def calcular(self, valor):
#         if valor < 0 or not isinstance(valor, int):
#             raise ValueError("El factorial solo se puede calcular para números enteros positivos.")
#         return math.factorial(valor)


# print("Seleccione la operación que desea realizar:")
# print("1. Raíz Cuadrada")
# print("2. Potencia")
# print("3. Logaritmo")
# print("4. Factorial")

# try:
#     opcion = int(input("Ingrese el número de la operación: "))

#     if opcion == 1:
#         valor = float(input("Ingrese el número para la raíz cuadrada: "))
#         resultado = RaizCuadrada().calcular(valor)
#         print(f"Raíz cuadrada de {valor}: {resultado:.2f}")
    
#     elif opcion == 2:
#         base = float(input("Ingrese la base: "))
#         exponente = float(input("Ingrese el exponente: "))
#         resultado = Potencia().calcular(base, exponente)
#         print(f"{base} elevado a la {exponente}: {resultado:.2f}")
    
#     elif opcion == 3:
#         valor = float(input("Ingrese el número para el logaritmo: "))
#         base = float(input("Ingrese la base del logaritmo (por defecto e): ") or math.e)
#         resultado = Logaritmo().calcular(valor, base)
#         print(f"Logaritmo base {base} de {valor}: {resultado:.2f}")
    
#     elif opcion == 4:
#         valor = int(input("Ingrese el número para el factorial: "))
#         resultado = Factorial().calcular(valor)
#         print(f"Factorial de {valor}: {resultado}")

#     else:
#         print("Opción no válida.")

# except ValueError as e:
#     print(f"Error: {e}")