#ejercicio 1 
# I = 1
# J = 2
# A = [0] * 11  

# A[I] = J      
# A[J] = I     
# A[J + I] = I + J  

# I = A[I] + A[J] 
# A[3] = 5        
# J = A[I] - A[J]  


# print("Valor final de I:", I)
# print("Valor final de J:", J)

#ejercicio 2

# X = 1
# Y = 2
# M = [1] * 5  

# M[X] = Y      
# M[Y] = X + 1  
# M[3] = M[1] + M[2]  

# X = M[3] - Y  
# Y = M[X] * 2  
# M[3] = Y  

# print("Valor final de X:", X)
# print("Valor final de Y:", Y)
# print("Valor final de M:", M[0:4])  


# ejercicio 3

# def leer_matriz():
#     matriz = []
#     for i in range(3):
#         try:
#             fila = input(f"Ingrese 3 números separados por espacio para la fila {i+1}: ").split()
            
#             if len(fila) != 3:
#                 raise ValueError("Debe ingresar exactamente 3 números por fila.")
            
#             fila = [float(num) for num in fila]  
#             matriz.append(fila)
        
#         except ValueError as e:
#             print(f"Error: {e}. Intente nuevamente.")
#             return leer_matriz() 
        
#         except Exception as e:
#             print(f"Error inesperado: {e}. Intente nuevamente.")
#             return leer_matriz()
    
#     return matriz

# def calcular_sumas(matriz):
#     suma_filas = [sum(fila) for fila in matriz]
#     suma_columnas = [sum(matriz[i][j] for i in range(3)) for j in range(3)]
#     return suma_filas, suma_columnas


# matriz = leer_matriz()


# suma_filas, suma_columnas = calcular_sumas(matriz)


# print("\nMatriz ingresada:")
# for fila in matriz:
#     print(fila)

# print("\nSuma de cada fila:", suma_filas)
# print("Suma de cada columna:", suma_columnas)

#ejercicio  4
# import numpy as np

# def crear_tabla():
#     try:
#         tabla = np.random.uniform(1, 100, (5, 5))  
#         return tabla
#     except Exception as e:
#         print(f"Error inesperado al crear la tabla: {e}")
#         return None

# def obtener_indice():
#     try:
#         K = int(input("Ingrese un índice K (0 a 24): "))
#         if K < 0 or K >= 25:
#             raise ValueError("El índice K debe estar entre 0 y 24.")
#         return K
#     except ValueError as e:
#         print(f"Error: {e}. Intente nuevamente.")
#         return obtener_indice()
#     except Exception as e:
#         print(f"Error inesperado: {e}. Intente nuevamente.")
#         return obtener_indice()

# def dividir_tabla(tabla, K):
#     try:
#         fila_K = K // 5  
#         col_K = K % 5    
#         divisor = tabla[fila_K][col_K]

#         if divisor == 0:
#             raise ZeroDivisionError("El elemento T[K] es cero, lo que causaría una división por cero.")

#         nueva_tabla = tabla / divisor
#         return nueva_tabla
#     except ZeroDivisionError as e:
#         print(f"Error: {e}. No se puede dividir por cero.")
#         return None
#     except Exception as e:
#         print(f"Error inesperado: {e}")
#         return None

# tabla_original = crear_tabla()

# print("\nTabla original:")
# print(tabla_original)

# K = obtener_indice()

# tabla_nueva = dividir_tabla(tabla_original, K)

# if tabla_nueva is not None:
#     print("\nNueva tabla después de la división:")
#     print(tabla_nueva)


