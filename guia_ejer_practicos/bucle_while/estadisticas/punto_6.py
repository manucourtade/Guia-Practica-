
'''Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
Calcular la suma de los números ingresados y el promedio de los mismos.'''

acumulador = 0

while True:
    contador = 1

    numero = int(input('Ingrese el numero: '))
    acumulador += numero
    contador += 1

    salir = input('Quiere seguir ingresando numeros? (s/n): ').lower()

    if salir == 'n':
        break

promedio = acumulador / contador
print(f'Contador: {contador} | Suma: {acumulador} | Promedio: {promedio}')