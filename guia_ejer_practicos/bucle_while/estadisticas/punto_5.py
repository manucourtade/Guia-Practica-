# Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.

contador = 1
acumulador = 0

while contador <= 5:
    numero = int(input(f'Ingrese el número {contador}: '))
    acumulador += numero
    contador += 1

promedio = acumulador / 5

print(f'\nLa suma de los números es: {acumulador}')
print(f'El promedio de los números es: {promedio}')
