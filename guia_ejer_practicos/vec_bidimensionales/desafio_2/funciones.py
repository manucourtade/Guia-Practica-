import random as rm

CANTIDAD_LINEAS = 3
CANTIDAD_COCHES = 5


def matriz_legajos(cant_li, cant_co):
    matriz = [[0, 0, 0, 0, 0] for _ in range(cant_li)]
    
    for i in range(cant_li):
        for j in range(cant_co):
            matriz[i][j] = rm.randrange(1000, 5000)  
    return matriz


def cargar_planilla(matriz):
    num_legajo = int(input('Ingrese su número de legajo: '))
    monto_total = 0.0
    encontrado = False 

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if num_legajo == matriz[i][j]:
                encontrado = True
                break
        if encontrado:
            return f'{num_legajo} no se encuentra en nuestro sistema'


    while True:
        linea = int(input('Ingrese la línea del viaje: '))
        coche = int(input('Ingrese el coche donde realizó el viaje: '))
        recaudacion = float(input('Ingrese la recaudación: '))

        monto_total += recaudacion

        salir = input('¿Desea cargar otra recaudación? (s/n): ').lower()
        if salir == 'n':
            break

    return f'Legajo: {num_legajo} - Total recaudado: {monto_total:.2f} - Linea: {linea} - Coche: {coche}'


def matriz_recaudacion(n_lineas, n_coches, registros):

    matriz = [[0.0 for _ in range(n_coches)] for _ in range(n_lineas)]

    for linea, coche, monto in registros:
        matriz[linea - 1][coche - 1] += monto

    return matriz

def recaudacion_linea(matriz, linea):
    suma = 0
    for monto in matriz[linea]:
        suma += monto

    return f'Recaudación total de la línea {linea + 1}: {suma:.2f}'

def recaudacion_coche(matriz, coche):
    suma_total = 0
    for i in range(len(matriz)):
        suma_total += matriz[i][coche]  

    return f'Coche {coche + 1} - Recaudación total: {suma_total:.2f}'

def recaudacion_total(matriz):
    suma_total = 0.0
    for fila in matriz:
        for monto in fila:
            suma_total += monto
    return f'Recaudación total: ${suma_total:.2f}'


