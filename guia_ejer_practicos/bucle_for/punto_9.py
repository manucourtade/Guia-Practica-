
# Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. 
# Mostrar la cantidad de divisores encontrados.
num = int(input('Ingrese un numero: '))
divisores = 0
for n in range(1, num + 1):
    if num % n == 0:
        print(f'{n} es divisor de {num}')
        divisores += 1

print(f'Hay {divisores} divisores de {num}')

