# Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.
def es_primo(n:int) -> bool:
    for i in range(2, n):   
        if n % i == 0:
            return False
    return True

n: int = int(input('Ingrese un numero: '))

print(es_primo(n))