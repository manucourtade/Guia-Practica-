# Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.
nota = int(input('Ingrese una nota:'))

while 10 < nota or nota < 1:
    print('La nota debe estar comprendida entre 1 y 10 inclusive.')
    nota = int(input('Ingrese una nota:'))

print(f'Tu nota: {nota}')