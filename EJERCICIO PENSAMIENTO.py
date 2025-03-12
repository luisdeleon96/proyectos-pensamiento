# #EJERCICIO 1

# metros = int(input("¿Cuántos metros cúbicos de agua utilizó? "))
# habitantes = int(input("¿Cuántos habitantes hay? "))  


# if metros < 15:
#     tarifa = 5
# elif metros >= 15 and metros <= 30:

#     if habitantes > 3:
#         tarifa = 4
#     elif habitantes == 3:
#         tarifa = 4.5
#     else:
#         tarifa = 5
# else:
#     if habitantes > 5:
#         tarifa = 3.5
#     elif habitantes % 2 == 0:
#         tarifa = 4
#     else:
#         tarifa = 4.2


# costo_total = metros * tarifa


# print(f"El costo total del consumo de agua es: Q{costo_total:.2f}")

# #EJERCICIO 2

# ano_vehiculo = int(input("Ingrese el año del vehículo: "))
# placa_vehiculo = input("Ingrese el número de la placa del vehículo: ")

# ultimo_digito = int(str(placa_vehiculo)[-1])


# if ano_vehiculo >= 2001:
#     if ultimo_digito in [0, 2, 4, 6, 8]:
#         dia_restriccion = "lunes"
#         mensaje = "NO circula los lunes"
#     elif ultimo_digito in [1, 3, 5, 7, 9]:
#         dia_restriccion = "viernes"
#         mensaje = "NO circula los viernes"

 
#     if ano_vehiculo % 2 == 0:
#         restriccion_sabado = "solo circula hasta el mediodía los sábados"
#     else:
#         restriccion_sabado = "sin restricción los sábados"

  
#     import datetime
#     anio_actual = datetime.datetime.now().year
#     antiguedad = anio_actual - ano_vehiculo
#     if antiguedad > 25:
#         mantenimiento = "Advertencia: Mantenimiento obligatorio."
#     else:
#         mantenimiento = "Sin mantenimiento obligatorio."

   
#     print(f"El vehículo con placa {placa_vehiculo} ({ano_vehiculo}):")
#     print(f"  - {mensaje}")
#     print(f"  - {restriccion_sabado}")
#     print(f"  - {mantenimiento}")
# else:
#     print(f"El vehículo con placa {placa_vehiculo} ({ano_vehiculo}) no está sujeto a las restricciones.")