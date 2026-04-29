# pida una edad
# si es 18 o más:

# edad = int(input("Ingrese su edad: "))

# if edad >= 18:
#     print("Puede entrar")
# else:
#     print("No puede entrar")


# Si nota es 6 o más → "Excelente"
# Si está entre 4 y menos de 6 → "Aprobado"
# Si es menor a 4 → "Reprobado"
# Usa if, elif, else.

# nota = float(input("Ingrese una nota: "))

# if nota >= 6:
#     print("Excelente")
# elif nota >= 4 and nota < 6:
#     print("Aprobado")   
# else:
#     print("Reprobado") 


# pedir edad
# pedir si tiene entrada (si o no)
# Reglas:
# Si tiene 18 o más y tiene entrada → "Puede ingresar"
# Si no → "Acceso denegado"
# menor de edad → "No cumple edad mínima"
# no tiene entrada → "No tiene entrada"
# ambas cumplen → "Puede ingresar"

# edad = int(input("Ingrese su edad: "))
# entrada = input("Tiene su entrada? (si/no): ")

# if edad >= 18 and entrada == "si":
#     print("Puede ingresar")
# else:
#     print("Acceso denegado")

# edad = int(input("Ingrese su edad: "))

# entrada = input("Tiene su entrada? (si/no): ").lower()

# if edad >= 18: #extra
#     if entrada == "si":
#         print("Puede ingresar")
#     else:
#         print("No tiene entrada")
# else:
#     print("No cumple edad mínima")


# Pedir sueldo.
# Si sueldo es menor a 500000 → bono 50000
# Si está entre 500000 y 800000 → bono 30000
# Si es mayor a 800000 → sin bono

# sueldo = int(input("Ingrese su sueldo: "))

# if sueldo < 500000:
#     print("Su bono es de 50.000")
# elif sueldo >= 500000 and sueldo <= 800000:
#     print("Su bono es de 30.000")
# else:
#     print("No tiene bono")


# Programa que pida:
# usuario
# contraseña
# Si usuario es:
# admin
# y contraseña es:
# 1234
# mostrar: Acceso correcto
# si no: Credenciales incorrectas
# Extra desafío
# Agregar:
# si usuario está bien pero contraseña mal:
# Contraseña incorrecta
# si usuario está mal:
# Usuario no existe


# user = input("Ingrese su usuario: ").lower()
# password = int(input("Ingrese su contraseña: "))

# if user == "admin":
#     if password == 1234:
#         print("Acceso correcto")
#     else:
#         print("Contraseña incorrecta")
#         print ("Credenciales incorrectas")
# else:
#     print("Usuario no existe")


# menor a 10 → Hace frío
# entre 10 y 25 → Templado
# mayor a 25 → Hace calor

# temp = int(input("Ingrese la temperatura: "))

# if temp < 10:
#     print("Hace frio")
# elif temp < 25:
#     print("Templado")
# else:
#     print("Hace calor")


# hacer un programa que determine si un año es bisiesto:
# Reglas:
# Si es divisible por 400 → bisiesto
# Si es divisible por 100 → NO bisiesto
# Si es divisible por 4 → bisiesto
# Si no → no bisiesto
# año = int(input("Ingrese un año: "))

# if año % 400 == 0:
#     print("Es bisiesto")
# elif año % 100 == 0:
#     print("No es bisiesto")
# elif año % 4 == 0:
#     print("Es bisiesto")
# else:
#    print("No es bisiesto")


# Pedir un número.
# si es positivo:
# Positivo
# si es negativo:
# Negativo
# si es cero:
# Es cero

num = int(input("Ingrese un numero: "))

if num > 0:
    print("Positivo")
elif num < 0:
    print("Negativo")
else:
    print("Es cero")


# Pedir una edad.
# menor de 12 → Niño
# 12 a 17 → Adolescente
# 18 o más → Adulto

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño")
elif edad < 17:
    print("Adolescente")
else:
    print("Adulto")        