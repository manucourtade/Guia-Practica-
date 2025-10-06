# Cargar una lista con nombres
# Pedí al usuario que ingrese 5 nombres y guardalos en una lista. Mostrá el contenido de la lista al finalizar.

lista_nombres = []

for i in range(5):
    nombre = input(f'Ingrese el {i+1} nombre: ')
    lista_nombres.append(nombre)
print('LISTA NOMBRES')
print(lista_nombres)


