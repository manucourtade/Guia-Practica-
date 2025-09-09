# Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área.
b:float = float(input('Ingrese la base del rectangulo: '))
h:float = float(input('Ingrese la altura del rectangulo: '))

def area_rectangulo(b:float, h:float) -> float:
    return (b * h) / 2

print('El area de tu rectangulo es:', area_rectangulo(b, h))
