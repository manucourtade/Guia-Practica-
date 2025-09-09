
# Ingresar un número. Determinar si el número es primo o no.
num = int(input('Ingrese un numero: '))
divisores = 0

for n in range(1, num + 1):
    if num % n == 0:   # si es divisor
        divisores += 1

if divisores == 2:
    print(f'{num} ES PRIMO')
else:
    print(f'{num} NO ES PRIMO')