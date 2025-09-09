# Ingresar 10 números enteros. Determinar el máximo y el mínimo.

contador = 1
numero = int(input(f'Ingrese el numero {contador}: '))
numero_min = numero
numero_max = numero

while contador < 11:
    numero = int(input(f'Ingrese el numero {contador}: '))
    contador += 1

    if numero > numero_max:
        numero_max = numero
    elif numero < numero_min:
        numero_min = numero

print(f'Numero maximo: {numero_max}')
print(f'Numero minimo: {numero_min}')
