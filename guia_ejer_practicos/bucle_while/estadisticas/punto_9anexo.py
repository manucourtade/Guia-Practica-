
# ANEXO

'''Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos.'''

contador = 0
acumulador = 0
while True:
    numero = int(input('Ingrese un numero: '))
    acumulador += numero
    contador += 1

    salir = input('Desea seguir agregando numeros? (s/n): ').lower()

    if salir == 'n':
        if contador >= 5:
            break
        else:
            print(f'Tienes que ingresar 5 numeros! Te faltan {5 - contador}')
    
        
promedio = acumulador / contador
print(f'Suma {acumulador} | Promedio {promedio}')
