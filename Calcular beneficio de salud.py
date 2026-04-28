# Calcular beneficio de salud

beneficio = 0

sueldo = int(input("Ingrese su sueldo"))

if sueldo >= 400000 and sueldo <= 800000:
    beneficio += 200000
elif sueldo <= 1200000:
    beneficio += 400000
else:
    beneficio += 700000

print("1. Basico")
print("2. Medio")
print("3. Superior")
educacion = int(input("Ingrese su nivel educacional"))     

if educacion == 1:
    beneficio *= 1
elif educacion == 2:
    beneficio *= 1.2
else:
    beneficio *= 1.4

afiliacion = input("Ingrese su tipo de afiliacion (nacional/extranjero)")

if afiliacion == "nacional":
    beneficio += 150000
elif afiliacion == "extranjero":
    beneficio += 50000

print("Su beneficio es de: ", beneficio)
