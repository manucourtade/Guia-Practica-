
'''Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. 
Calcular la suma de los números ingresados y el promedio de los mismos.'''

contador = 0
acumulador = 0
while True:
    if contador == 10:
        print("⚠️ Ya alcanzaste el máximo de 10 números.")
        break

    numero = int(input('Ingrese un numero: '))
    acumulador += numero
    contador += 1

    if contador >= 5:  # recién a partir de 5 puede salir
        salir = input('¿Desea seguir agregando números? (s/n): ').lower()
        if salir == 'n':
            break
            
    
        
promedio = acumulador / contador
print(f'Suma {acumulador} | Promedio {promedio}')

