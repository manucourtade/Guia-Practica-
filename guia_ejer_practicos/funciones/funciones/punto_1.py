# Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

def num_entero() -> int:
    num = int(input('Ingrese un numero entero: '))
    return num

print(num_entero())
