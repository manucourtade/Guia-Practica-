# Ingresar un número y mostrar la tabla de multiplicar de ese número. 
num = int(input('Ingrese un numero: '))
for n in range(1, 10 + 1):
    print(f' {num} x {n} = {num * n}')
