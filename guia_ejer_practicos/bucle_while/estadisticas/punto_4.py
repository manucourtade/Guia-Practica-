# Mostrar la suma de los números pares desde el 1 hasta el 10.

contador = 1
acumulador = 0

while contador < 11:
    if contador % 2 == 0:
        print(f'\nContador: {contador} | {acumulador} + {acumulador} = {acumulador + acumulador}')
        acumulador += contador
    contador += 1