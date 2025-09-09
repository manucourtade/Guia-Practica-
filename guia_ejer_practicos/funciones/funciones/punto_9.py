# Diseña una función que calcule la potencia de un número. La función debe recibir la base 
# y el exponente como argumentos y devolver el resultado.
def calc_potencia(b:int, exp:int) -> int:
    return b**exp

base:int = int(input('Ingrese la base del numero:'))
exponente:int = int(input('Ingrese el exponente del numero:'))

print(f'Base: {base}, Exp.: {exponente} =',calc_potencia(base,exponente))