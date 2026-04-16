suma = 0
cantidad = 0

num = int(input('Ingrese un numero (0 para finalizar): '))

while num != 0:
    suma += num
    cantidad += 1
    num = int(input('Ingrese un numero (0 para finalizar): '))

print ('La suma de todos los numeros es:', suma)
print ('La cantidad de numeros ingresados es:', cantidad)