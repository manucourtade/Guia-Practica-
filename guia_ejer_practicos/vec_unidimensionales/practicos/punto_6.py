# Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.
def max_valor(list_int):
    valor_max = 0
    for i in range(len(list_int)):
        if list_int[i] > valor_max:
            valor_max = list_int[i]
    return f'Valor maximo encontrado {valor_max}'

print(max_valor([10, 2320, 30, 456]))