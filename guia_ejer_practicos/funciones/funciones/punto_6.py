# Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
def es_par(num:int) -> int:
    if num % 2 == 0:
        return f'{num} es par'
    else:
        return f'{num} es impar'

n:int = int(input('Ingrese un numero: '))

print(es_par(n))