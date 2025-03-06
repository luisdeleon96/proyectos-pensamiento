#1
palabra="Python es un lenguaje poderoso porque si " 

palabra2=palabra.split()
print(palabra2)



palabra3=len(palabra2)
print(palabra3)

print(palabra2[0])
print(palabra2[-1])

#2
palabra="Hola          mundo  en  Python"

palabra2=palabra.split()
print(palabra2)

palabra3=" ".join(palabra2)
print(palabra3)

#3
palabra= "usuario@gmail.com"
palabra2=palabra.split()
print(palabra2)

palabra3=palabra.split("@")
print(palabra3)

#4
palabra="documento.pdf"
palabra2=palabra.split()
print(palabra2)
 
palabra3=palabra.endswith("pdf")
print(palabra3)


#5
palabra="Me gusta Python"
palabra2=palabra.split()
print(palabra2)

palabra3=  ",".join(palabra2)
print(palabra2[::-1])

#6
palabra=input("ingrese que desea saber")
palabra2=palabra.split()
print(palabra2)

poema1="Podrá nublarse el sol eternamente; Podrá secarse en un instante el mar;Podrá romperse el eje de la tierra Como un débil cristal.”

canto1="Eres como la noche, callada y constelada.Tu silencio es de estrella, tan lejano y sencillo .Me gustas cuando callas porque estás como ausente.Distante y dolorosa como si hubieras muerto."

if "poema" in (palabra2):
    print(poema1)

if "canto" in (palabra2):
    print(canto1)
