
# num = int(input("Ingrese un numero: "))

# while num != int:
#     num = int(input("Error, numero no valido. Ingrese un numero: "))

# if num > 0:
#     print("El numero es positivo")
# elif num < 0:
#     print("El numero es negativo")
# else:
#     print("El numero es cero")



# import random

# intentos = 0
# num = random.randint(1, 20)

# acierto = int(input("Ingrese el numero a adivinar: "))

# while acierto != num:
#     if acierto > num:
#         print("Muy alto")
#     elif acierto < num:
#         print("Muy bajo")
#     intentos += 1
#     acierto = int(input("Ingrese el numero a adivinar: "))

# print(f"Has adivinado el numero en {intentos} intentos")


# num = 0
# tnum = 0
# suma = 0
# op = 0

# while op != 4:
#     print("1. Agregar numero")
#     print("2. Mostrar suma total")
#     print("3. Mostrar promedio")
#     print("4. Salir")
#     op = int(input("Seleccione una opcion: "))

#     match op:
#         case 1:
#             print("Agregando numeros")
#             num = float(input("Ingrese un numero a agregar: "))
#             suma += num
#             tnum += 1
#         case 2:
#             print("Mostrando suma total")
#             if tnum == 0:
#                 print("Error, no ha ingresado numeros para mostrar")
#             else:
#                 print(f"La suma de los numeros ingresados es: {suma}")
#         case 3:
#             print("Mostrando promedio")
#             if tnum == 0:
#                 print("Error, no ha ingresado numeros para mostrar")
#             else:
#                print(f"El promedio de los numeros ingresados es: {suma / tnum}")
#         case _:
#             print("Opcion invalida")    



# import random

# suma = 0
# op = 0
# tlanzamientos = 0

# while op != 3:
#     print("1. Lanzar dado")
#     print("2. Ver estadisticas")
#     print("3. Salir")
#     op = int(input("Seleccione una opcion: "))
#     match op:
#         case 1:
#             print("El dado ha sido lanzado")
#             num = random.randint(1, 6)
#             print(f"Ha salido un: {num}")
#             tlanzamientos += 1
#             suma += num
#         case 2:
#             print("Viendo estadisticas")    
#             if tlanzamientos == 0:
#                 print("No hay lanzamientos registrados")
#             else:
#                 print(f"El total de lanzamientos es: {tlanzamientos}")    
#                 print(f"El promedio de los valores obtenidos es: {suma / tlanzamientos}")
#         case 3:
#             print("Gracias por jugar")    
#         case _:
#            print("Opcion invalida")    



# suma = 0
# pares = 0

# num = int(input("Ingrese un numero: "))

# if num <= 0:
#     print("Error, el numero no puede ser menor o igual a cero")
# else:
#     for i in range(1, num + 1):
#         if i % 2 == 0:
#             suma += i
#             pares += 1

#     print(f"La suma de los numeros pares es: {suma}")
#     print(f"La cantidad de numeros pares es: {pares}")



# import random

# canti6 = 0
# suma = 0

# lanz = int(input("Seleccione la cantidad de lanzamientos: "))

# if lanz <= 0:
#     print("Error, el numero no puede ser menor o igual a cero")
# else:
#    for i in range(1, lanz + 1):
#         giro = random.randint(1, 6)
#         print(f"Lanzamiento {i}: {giro}")

#         suma += giro
# 
#         if giro == 6:
#             canti6 += 1

#     print(f"Suma total: {suma}")
#     print(f"Promedio: {suma / lanz}")
#     print(f"El numero 6 salio {canti6} veces")



# suma = 0
# cnotas = 0
# op = 0
# aprobados = 0

# while op != 4:
#     print("1. Ingresar nota")
#     print("2. Ver promedio")
#     print("3. Ver cantidad de aprobados")
#     print("4. Salir")
#     op = int(input("Seleccione una opcion: "))
#     match op:
#         case 1:
#             nota = float(input("Ingrese la nota: (ej: 1.0, 7.0) "))
#             suma += nota
#             cnotas += 1
#             if nota >= 4.0:
#                 aprobados += 1
#         case 2:
#             if cnotas == 0:
#                 print("Error, no hay notas")
#             else:    
#                 print(f"El promedio de las notas es: {suma / cnotas}")
#         case 3:
#             print(f"La cantidad de aprobados es: {aprobados}")
#         case 4:
#             print("Saliendo")    
#         case _:
#             print("Opcion invalida") 



alumnos = int(input("Ingrese cantidad de alumnos: "))
notas = int(input("Ingrese cantidad de notas por alumno: "))

for i in range(1, alumnos + 1):
    print(f"\nAlumno {i}")

    suma = 0

    for j in range(1, notas + 1):
        nota = float(input(f"Ingrese nota {j}: "))
        suma += nota

    promedio = suma / notas
    print(f"Promedio del alumno {i}: {promedio}")