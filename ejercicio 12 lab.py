# dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
# azucar = [130, 160, 95, 175, 160]
# sal = [2000, 2400, 1800, 2400, 2700]
# presion = [(115, 75), (130, 80), (110, 70), (125, 85), (175, 95)]

# def promedio(lista):
#     return sum(lista) / len(lista)

# def estado_presion(sistolica, diastolica):
#     if sistolica < 120 and diastolica < 80:
#         return "Normal"
#     elif 120 <= sistolica <= 129 and diastolica < 80:
#         return "Elevada"
#     elif 130 <= sistolica <= 139 or 80 <= diastolica <= 89:
#         return "Hipertensión 1"
#     elif sistolica >= 140 or diastolica >= 90:
#         return "Hipertensión 2"
#     return "Fuera de rango"

# for i in range(len(dias)):
#     print(f"{dias[i]}:")
#     print(f"  Azúcar: {azucar[i]} mg/dL ({'Normal' if 70 <= azucar[i] <= 140 else 'Fuera de rango'})")
#     print(f"  Sal: {sal[i]} mg ({'Normal' if sal[i] <= 2300 else 'Exceso'})")
#     print(f"  Presión: {presion[i][0]}/{presion[i][1]} mmHg ({estado_presion(presion[i][0], presion[i][1])})")

# print("\nPromedios semanales:")
# print(f"  Azúcar: {promedio(azucar):.2f} mg/dL")
# print(f"  Sal: {promedio(sal):.2f} mg")
# print(f"  Presión: {promedio([p[0] for p in presion]):.2f}/{promedio([p[1] for p in presion]):.2f} mmHg")