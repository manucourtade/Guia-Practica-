
# Integrador While

'''
Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
La suma acumulada de los números negativos.
La suma acumulada de los números positivos.
La cantidad de números negativos ingresados.
El promedio de los números positivos.
El número positivo más grande.
El porcentaje de números negativos ingresados, respecto del total de ingresos.
'''

contador_neg = 0
acumulador_neg = 0
acumulador_pos = 0
contador_pos = 0
numero_max = None
promedio = 0
porcentaje = 0
total_numeros = 0

while True:
    numero = int(input('Ingrese el numero:'))
    total_numeros += 1

    if numero < 0:
        acumulador_neg += numero
        contador_neg += 1
    else:
        acumulador_pos += numero
        contador_pos += 1

        if numero_max is None or numero > numero_max:
            numero_max = numero

        if contador_pos > 0:
            promedio = acumulador_pos / contador_pos

    porcentaje = (contador_neg / total_numeros) * 100

    salir = input('Desea seguir agregando numeros? (s/n): ').lower()

    if salir == 'n':
        break

print(f''' 
La suma acumulada de los números negativos. {acumulador_neg}
La suma acumulada de los números positivos. {acumulador_pos}
La cantidad de números negativos ingresados. {contador_neg}
El promedio de los números positivos. {promedio:.1f}
El número positivo más grande. {numero_max}
El porcentaje de números negativos ingresados, respecto del total de ingresos. {porcentaje}%''')