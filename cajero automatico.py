saldo = 3000
intentos = 3

while saldo > 0:
    monto = input("Ingrese monto a retirar: ").strip()
    
    if monto == "0":
        print("Adiós")
        break
    
    if not monto.replace(" ", "").isdigit():
        print("Ingrese un número válido.")
        continue
    
    monto = int(monto)
    
    if monto > saldo:
        intentos -= 1
        print("Saldo insuficiente. Intentos restantes:", intentos)
        if intentos == 0:
            print("Demasiados intentos fallidos. Adiós.")
            break
    else:
        saldo -= monto
        if saldo == 0:
            print("Retiro exitoso. Saldo agotado. Adiós")
            break
        else:
            print("Retiro exitoso. Nuevo saldo:", saldo)