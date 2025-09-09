# Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.
def es_par(n:int) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False