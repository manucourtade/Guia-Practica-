# Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), 
# muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. 
# La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.

def es_primo(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def primos_hasta(limite: int) -> int:
    contador_primos = 0
    for n in range(2, limite + 1):
        if es_primo(n):
            print(n, end=" ")   # mostramos el primo
            contador_primos += 1
    print()  # salto de línea
    return contador_primos


# Programa principal
num = int(input("Ingrese un número: "))
cantidad = primos_hasta(num)
print(f"Cantidad de números primos encontrados: {cantidad}")
