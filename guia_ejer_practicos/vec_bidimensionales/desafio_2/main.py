# 📌 Desafío: Gestión de Recaudaciones en una Empresa de Colectivos

from funciones import *

def gestor_recaudaciones():
    legajos = matriz_legajos(CANTIDAD_LINEAS, CANTIDAD_COCHES)

    while True:
        opcion = input('''
Ingrese una opcion:
1. Cargar planilla de recaudación
2. Mostrar la recaudacion de cada coche y linea
3. Calcular y mostrar la recaudacion por linea
4. Calcular y mostrar la recaudacion por coche
5. Calcular y mostrar la recaudacion total
6. Salir 
=> ''')
        
        if opcion == '1':
            chofer = cargar_planilla(legajos)
            print(chofer)
        
        elif opcion == '2':
            matriz_recaudacion(CANTIDAD_LINEAS, CANTIDAD_COCHES, legajos)

        elif opcion == '3':
            recaudacion_linea(legajos, CANTIDAD_LINEAS)

        elif opcion == '4':
            recaudacion_coche(legajos, CANTIDAD_COCHES)

        elif opcion == '5':
            recaudacion_total(legajos)

        elif opcion == '6':
            print('ADIOS...')
            break

        else:
            print('Seleccione una opcion correcta')

gestor_recaudaciones()