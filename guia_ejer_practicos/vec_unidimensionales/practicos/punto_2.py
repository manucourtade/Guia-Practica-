# Escribir una función que permita ingresar la cantidad de números que reciba como parámetro.  Crear el array con la función del punto 1.

# Punto 1
def crear_array(cant):
    return [0] * cant
    

def ingresar_cant():
    num = int(input('Ingresar la cantidad de elementos de array: '))
    return num

num = ingresar_cant()
print(crear_array(num))
