# Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones 
# en donde se encuentra el valor máximo hallado.
def posicion_valor_max(list_int):
    valor_max = 0
    for i in range(len(list_int)):
        if list_int[i] > valor_max:
            valor_max = list_int[i]

    posiciones = "" 
    for i in range(len(list_int)):
        if list_int[i] == valor_max:
            posiciones += str(i + 1) + ", "
        
    return f"Valor max: {valor_max} en las posiciones {posiciones}"


print(posicion_valor_max([10, 2320, 30, 2320]))