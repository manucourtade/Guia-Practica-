# Buscar el índice de un elemento
# Pedir un nombre al usuario, buscar si se encuentra en la lista y mostrá el índice en el que se encuentra
# usando index(). Si no se encuentra mostrar un cartel aclaratorio

lista_nombres = []

for i in range(5):
    nombre = input(f'Ingrese el {i+1} nombre: ').capitalize()
    lista_nombres.append(nombre)
print('LISTA NOMBRES')
print(lista_nombres)

nombre_buscar = input('Ingrese nombre a buscar: ').capitalize()

if nombre_buscar in lista_nombres:
    pos = lista_nombres.index(nombre_buscar)
    print(f'{nombre_buscar} se encuentra en la posicion {pos}')
else:
    print('No se encontro cuyo nombre')
