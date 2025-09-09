# Crear una función que le solicite al usuario el ingreso de una cadena y la retorne.

def pedir_cadena() -> str:
    cadena = input('Ingrese un texto: ')
    return cadena

print('Texto:', pedir_cadena())