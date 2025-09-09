# Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro.
#  La función debe aceptar parámetros opcionales (inicio y fin)
#  para definir el rango de multiplicación. Por defecto es del 1 al 10.

def tabla_multiplicar(num:int, incio:int = 1, fin:int = 10) -> int:
        print(f'\nTABLA DE MULTIPLICAR DEL {num}\n')
        for i in range(incio, fin + 1):
            print(f'{num} x {i} = {num * i}')
        

num:int = int(input('Ingrese un numero: '))

tabla_multiplicar(num)