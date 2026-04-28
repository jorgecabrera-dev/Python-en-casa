# calcular el puntaje de credito

credito = 0

sueldo = int(input("Ingrese su sueldo aproximado"))

if sueldo >= 500000 and sueldo <= 1000000:
    credito = 300000
if sueldo <= 1500000:
    credito = 6500000
else:
    credito = 100000 

print("1. Basico")
print("2. Medio")
print("3. Superior")

educacion = int(input("Ingrese su nivel educacional "))

if educacion == "1":
    credito += credito * 1
if educacion == "2":
    credito += credito * 1.3
if educacion == "3":
    credito += credito * 1.5

nacionalidad = input("Ingrese su nacionalidad (chilena/extranjero)")

if nacionalidad == "chilena" or "chileno":
    credito += 300000
if nacionalidad == "extranjero" or "extranjera":
    print("No hay bono por nacionalidad")

print("Su credito es: ", credito)




              