# 1
# n= int(input("coloque su numero: "))
# def es_par(n):
#     if n % 2 == 0:
#         print("es par")
#     else:
#         print("es impar")

# es_par(n)

# 2
# def suma_lista():
#     numeros = input("Ingrese los números separados por espacios: ") 
#     lista = [int(numero) for numero in numeros.split()] 
#     suma = sum(lista) 
#     return suma

# resultado = suma_lista()
# print(f"La suma de los números es: {resultado}")

# 3
# def cuenta_regresiva(n):
#     if n <0:
#         print("despegar")
#     else:
#         print(n)
#         cuenta_regresiva(n-1)
# cuenta_regresiva(int(input("ingrese el numero: ")))

# 4
# def cuenta_ascendente(n):
#     for i in range(1, n+1): 
#         print(i) 
# numero = int(input("Ingrese el número: ")) 
# cuenta_ascendente(numero)

# 5
# def suma_hasta(n):
#     if n == 0:
#         return 0
#     else:
#         return n + suma_hasta(n - 1)

# print(suma_hasta(4))

# 6
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))


# 7
# def minimo(lista):
#     if len(lista) == 1:
#         return lista[0]
#     else:
#         menor = minimo(lista[1:])
#         return lista[0] if lista[0] < menor else menor

# print(minimo([5, 3, 8, 1, 2]))

import time

def adivina_el_numero(numero_secreto, intentos, tiempo_inicio):
    if intentos == 0:
        print("¡Se acabaron los intentos! El número era:", numero_secreto)
        print("Tiempo total: {:.2f} segundos.".format(time.time() - tiempo_inicio))
        return

    try:
        intento = int(input(f"Te quedan {intentos} intento(s). Ingresa tu número: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        adivina_el_numero(numero_secreto, intentos, tiempo_inicio)
        return

    if intento == numero_secreto:
        tiempo_final = time.time()
        print(f"¡Felicidades! Adivinaste el número {numero_secreto} correctamente.")
        print("Lo lograste en {:.2f} segundos.".format(tiempo_final - tiempo_inicio))
    elif intento < numero_secreto:
        print("Demasiado bajo.")
        adivina_el_numero(numero_secreto, intentos - 1, tiempo_inicio)
    else:
        print("Demasiado alto.")
        adivina_el_numero(numero_secreto, intentos - 1, tiempo_inicio)

# Inicio del juego
import random
numero_secreto = random.randint(1, 100)

print("Bienvenido al juego de Adivina el Número.")
print("Elige un número entre 1 y 100.")
print("¡Buena suerte!")

tiempo_inicio = time.time()
adivina_el_numero(numero_secreto, 5, tiempo_inicio)
