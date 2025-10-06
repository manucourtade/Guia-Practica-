# Uso de in y conversión
# Dada la tupla colores = ('rojo', 'verde', 'azul'), hacer lo siguiente:
# ● Verificar si el color 'amarillo' está en la tupla.
# ● Convertir la tupla en una lista, agregar el color 'amarillo', y volver a convertirla en tupla.
# ● Mostrar la nueva tupla resultante.

colores = ('rojo', 'verde', 'azul')

if 'amarillo' in colores:
    print('Amarillo se encuentra en la tupla')
else:
    print('Amarillo no se encuentra en la lista')
    
colores = list(colores)

colores.append('amarillo')

colores = tuple(colores)

print('Nueva tupla resultante')
print(colores)
