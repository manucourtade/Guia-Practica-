import funciones as fn



def recomendacion_productos():
    usuario1, usuario2 = fn.ingresar_datos()

    while True:
        opcion = input('''
1. Productos en comun
2. Productos exclusivos
3. Catalogo total
4. Recomendaciones''')
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
            reco = fn.recomendacion()
            print(reco)

recomendacion_productos()