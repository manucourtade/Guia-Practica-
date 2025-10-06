#Eliminar un nombre usando remove()
#Solicitá al usuario un nombre a eliminar. Si el nombre está en la lista, removelo. Si no está, mostrá un mensaje.

lista_nombres = []

for i in range(5):
    nombre = input(f'Ingrese el {i+1} nombre: ')
    lista_nombres.append(nombre)
print('LISTA NOMBRES')
print(lista_nombres)

nombre_eliminado = input('Ingrese el nombre a eliminar: ')

if nombre_eliminado in lista_nombres:
    lista_nombres.remove(nombre_eliminado)
else:
    print('No se encuentra en la lista ese nombre!')
print(f'LISTA NUEVA, se elimino {nombre_eliminado}')
print(lista_nombres)

