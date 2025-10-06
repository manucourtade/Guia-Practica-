# Insertar un nuevo nombre en una posición específica
# Usá el método insert() para agregar un nombre nuevo en la segunda posición (índice 1) de la lista anterior.

lista_nombres = []

for i in range(5):
    nombre = input(f'Ingrese el {i+1} nombre: ')
    lista_nombres.append(nombre)
print('LISTA NOMBRES')
print(lista_nombres)

nombre_nuevo = input('Ingrese el nombre nuevo: ')
lista_nombres.insert(1, nombre_nuevo)
print('LISTA NUEVA')
print(lista_nombres)


