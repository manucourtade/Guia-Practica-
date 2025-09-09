# Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.
contador = 0
acumulador = 0

for n in range(10):
    num = int(input('Ingrese un numero: '))

    if num == 0:
        break

    contador += 1
    acumulador += num

    if contador > 0:
        promedio = acumulador / contador
    else:
        promedio = 0
    
print(f'Suma {acumulador}, promedio {promedio}')
