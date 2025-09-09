
# Realizar un programa que permita mostrar una pirámide de números.
# Pedimos al usuario la cantidad de filas
filas = int(input("Ingrese el número de filas de la pirámide: "))

for i in range(filas + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print() 