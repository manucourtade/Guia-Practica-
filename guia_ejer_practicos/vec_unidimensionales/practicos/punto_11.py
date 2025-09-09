# Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la diferencia de los dos arrays.
conjuntoM = ['a', 'c', 'b']
conjuntoN = ['l', 'g', 'b', 'e', 'i', 'h', 'j', 'f']

def recibir_diferencia(array1, array2):
    diferencia = []
    for i in range(len(array1)):
        esta_en_N = False
        for j in range(len(array2)):
            if array1[i] == array2[j]:
                esta_en_N = True
        if not esta_en_N:   # si no está en N, lo guardo
            diferencia += [array1[i]]
    return f'Diferencia M - N: {diferencia}'

print(recibir_diferencia(conjuntoM, conjuntoN))
