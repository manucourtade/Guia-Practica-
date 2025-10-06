# Usar el operador in
# Mostrá un mensaje indicando si el nombre "Juan" está o no en la lista.

lista_nombres = []

for i in range(5):
    nombre = input(f'Ingrese el {i+1} nombre: ').capitalize()
    lista_nombres.append(nombre)
print('LISTA NOMBRES')
print(lista_nombres)

if 'Juan' in lista_nombres:
    print('Juan se encuentra en la lista')
else:
    print('No se encontro Juan en la lista')