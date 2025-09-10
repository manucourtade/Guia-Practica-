import funciones as fn

usuario1 = ['Arroz', 'Atun', 'Queso', 'Tomate', 'Leche']
usuario2 = ['Tomate', 'Huevo', 'Cebolla', 'Atun', 'Burrata']

def recomendacion_productos():
    while True:
        opcion = input('''
1. Productos en comun
2. Productos exclusivos
3. Catalogo total
4. Recomendaciones
5. Salir
=> ''')
        if opcion == '1':
            producto_comun = fn.productos_comun(usuario1, usuario2)
            print(f'Productos en comun:')
            print(producto_comun)

        elif opcion == '2':
            exclusivo1, exclusivo2 = fn.productos_exclusivos(usuario1, usuario2)
            print('Producots exclusivos')
            print(f'Usuario 1:\n',exclusivo1)
            print(f'Usuario 2:\n',exclusivo2)

        elif opcion == '3':
            conjunto = fn.catalogo_total(usuario1, usuario2)
            print('Catalogo total:')
            print(conjunto)

        elif opcion == '4':
            r1, r2 = fn.recomendar(usuario1, usuario2)

            print("Recomendaciones para el usuario 1:", r1)
            print("Recomendaciones para usuario 2:", r2)
        
        elif opcion == '5':
            print('Adios!')
            break
        
        else:
            print('Por favor ingrese numeros del 1 al 5!')

recomendacion_productos()