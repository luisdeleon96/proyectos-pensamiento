def imprimir_tablero(matriz):
#     for fila in matriz:
#         print(" ".join(str(celda) for celda in fila))
#     print()

# def siguiente_generacion(matriz):
#     filas = len(matriz)
#     columnas = len(matriz[0])
#     nueva_matriz = [[0] * columnas for _ in range(filas)]

#     for i in range(filas):
#         for j in range(columnas):
#             vecinos_vivos = 0
            
#             # Verificar vecinos izquierdo y derecho
#             if j > 0 and matriz[i][j - 1] == 1:
#                 vecinos_vivos += 1
#             if j < columnas - 1 and matriz[i][j + 1] == 1:
#                 vecinos_vivos += 1

#             # Aplicar reglas
#             if matriz[i][j] == 1:  # Celda viva
#                 if vecinos_vivos == 1 or vecinos_vivos == 2:
#                     nueva_matriz[i][j] = 1
#                 else:
#                     nueva_matriz[i][j] = 0
#             else:  # Celda muerta
#                 if vecinos_vivos == 1:
#                     nueva_matriz[i][j] = 1

#     return nueva_matriz


# matriz = [
#  [0,0,0,0,0,0,0,1,1,0],
#  [0,1,1,0,0,0,0,0,0,0],
#  [0,1,0,0,0,0,0,0,0,0],
#  [0,0,0,0,0,0,0,0,0,0],
#  [0,0,0,0,0,0,0,0,0,0],
#  [0,0,0,0,0,1,1,0,0,0],
#  [0,0,0,0,0,1,1,0,0,0],
#  [0,0,1,1,0,0,0,0,0,0],
#  [0,0,1,1,0,0,0,0,0,0],
#  [0,0,0,0,0,0,0,0,1,0],
# ]


# print("Generación 0:")
# imprimir_tablero(matriz)

# generacion_1 = siguiente_generacion(matriz)
# print("Generación 1:")
# imprimir_tablero(generacion_1)

# generacion_2 = siguiente_generacion(generacion_1)
# print("Generación 2:")
# imprimir_tablero(generacion_2)