# Mostrar la suma de los números desde el 1 hasta el 10.

contador = 1
acumulador = 1

while contador < 11:
    print(f'Contador: {contador} | {acumulador} + {acumulador} = {acumulador + acumulador}')
    acumulador += 1
    contador += 1