# #EJERCICIO 1
# for i in range(1, 11):
#     if i % 2 != 0:  
#         print(i)  

# #EJERCCIO 2
# x = 1
# while x < 11:
#     if x % 2 != 0:  
#         print(x)  
#     x += 1  

# #ESCENARIO 1
# while True:
#     palabra = input("Ingresa una palabra: ")
#     if palabra == "chupacabra": 
#         print("¡Has dejado el bucle con éxito!")
#         break  

# #ESCENARIO 2
# user_word = input("Ingresa una palabra: ")
# user_word = user_word.upper()  

# for letter in user_word:
#     if letter in 'AEIOU':  
#         continue  
#     print(letter)  

# #ESCENARIO 3
# bloques = int(input("Ingresa la cantidad de bloques: "))


# altura = 0
# capa = 1


# while bloques >= capa:
#     bloques -= capa  
#     altura += 1 
#     capa += 1 
# print("La altura de la pirámide es:", altura)