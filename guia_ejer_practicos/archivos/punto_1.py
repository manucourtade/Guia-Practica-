lista_productos = [
    ['P001', 'LARGA VIDA', 'ALIMENTOS', 2500, 20],
    ['P002', 'PEPITOS', 'ALIMENTOS', 2000, 14],
    ['P003', 'FERNET BRANCA', 'BEBIDAS ALCOHOLICAS', 15999, 31],
    ['P004', 'LATON BRAHMA', 'BEBIDAS ALCOHOLICAS', 2500, 12],
    ['P005', 'TRAPO DE GAMUSA', 'LIMPIEZA', 1500, 10],
    ['P006', 'PERFUME PACO', 'BELLEZA', 8500, 30],
    ['P007', 'PAPEL HIGIENICO ELITE', 'HIGIENE', 3000, 40],
    ['P008', 'FLANDRIA YELLOW', 'TABAQUERIA', 9600, 10]
]

nombre_archivo = 'ventas.csv'

def cargar_archivos(archivo):
    with open(archivo, 'w', encoding='utf-8') as ventas:
        ventas.write('Código,Nombre,Categoría,Precio,Stock\n')

        for producto in lista_productos:
            linea = ''  
            for i in range(len(producto)):
                linea += str(producto[i])  
                if i < len(producto) - 1:  
                    linea += ','
            ventas.write(linea + '\n')

    print("✅ Archivo 'ventas.csv' creado correctamente.")

def leer_archivo(archivo):
    with open(archivo, 'r') as ventas:
        lineas = ventas.readlines()

    print(f'{"ID":<6} {"NOMBRE":<25} {"CATEGORIA":<25} {"PRECIO":<10} {"STOCK":<10}')
    print('-' * 80)

    for linea in lineas[1:]:
        datos = linea.strip().split(',')  
        print(f'{datos[0]:<6} {datos[1]:<25} {datos[2]:<25} {datos[3]:<10} {datos[4]:<10}')

def calcular_totales(archivo):
    with open(archivo, 'r', encoding='utf-8') as ventas:
        lineas = ventas.readlines()

    suma_stock = 0
    suma_precio = 0
    contador = 0

    for linea in lineas[1:]:  # saltamos el encabezado
        datos = linea.strip().split(',')
        precio = float(datos[3])
        stock = int(datos[4])

        suma_precio += precio
        suma_stock += stock
        contador += 1

    promedio = suma_precio / contador  # promedio de precios

    resumen = {
        'total_unidades': suma_stock,
        'monto_total': suma_precio,
        'promedio_precio': promedio
    }

    print(f'TOTAL DE UNIDADES: {resumen["total_unidades"]}')
    print(f'MONTO TOTAL RECAUDADO: ${resumen["monto_total"]:.2f}')
    print(f'PROMEDIO DE PRECIO DE LOS PRODUCTOS: ${resumen["promedio_precio"]:.2f}')

def filtrar_generar(archivo):
    with open(archivo, 'r') as ventas:
        lineas = ventas.readlines()

    productos_destacados = []
    contador = 0

    for linea in lineas[1:]:  # Ignoramos el encabezado
        datos = linea.strip().split(',')
        stock = int(datos[4])
        if stock > 20:
            productos_destacados.append(datos)
            contador += 1

    # Guardar en un nuevo archivo
    with open('ventas_destacadas.csv', 'w') as destacado:
        destacado.write(lineas[0])  # escribimos el encabezado
        for producto in productos_destacados:
            linea = ''
            for i in range(len(producto)):
                linea += str(producto[i])
                if i < len(producto) - 1:  # poner coma entre elementos, menos al final
                    linea += ','
            destacado.write(linea + '\n')  # escribimos en el archivo correcto

    print(f'Fueron exportados {contador} productos!')



def actualizar_datos(archivo):
    buscar = input('Ingrese la categoria a buscar: ').strip().lower()

    with open(archivo, 'r') as ventas:
        lineas = ventas.readlines()

    encabezado = lineas[0]
    nuevas_lineas = [encabezado]
    encontrados = 0

    for linea in lineas[1:]:
        datos = linea.strip().split(',')
        categoria = datos[2].lower()
        precio = float(datos[3])

        if categoria == buscar:
            precio = precio * 1.10
            datos[3] = f'{precio:.2f}'
            encontrados += 1

        # Construimos la línea manualmente sin join
        linea_nueva = ''
        for i in range(len(datos)):
            linea_nueva += str(datos[i])
            if i < len(datos) - 1:
                linea_nueva += ','
        linea_nueva += '\n'  # agregamos salto de línea
        nuevas_lineas.append(linea_nueva)

    if encontrados == 0:
        print('No se encontró la categoría!')
    else:
        with open(archivo, 'w') as ventas:
            ventas.writelines(nuevas_lineas)
        print(f'Se actualizaron {encontrados} productos de la categoría "{buscar}".')




actualizar_datos('ventas.csv')
