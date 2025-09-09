# Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

def area_circulo(radio:float) -> float:
    return 3.14 * (radio**2)

radio:float = float(input('Ingrese el radio del circulo: '))

print('Area del circulo:', area_circulo(radio))