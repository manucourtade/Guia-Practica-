# Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

def num_flotante() -> float:
    num = float(input('Ingrese un numero flotante: '))
    return num

print(num_flotante())