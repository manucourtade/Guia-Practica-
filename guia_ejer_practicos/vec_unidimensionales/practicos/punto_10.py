# Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la unión de los dos arrays.

conjuntoM = ['a', 'c', 'b', 'j', 'f']
conjuntoN = ['l', 'g', 'b', 'e', 'i', 'h']

def recibir_union(array1, array2):
    union = []

    for i in range(len(array1)):
        union += [array1[i]]

    for j in range(len(array2)):
        existe = False
        for k in range(len(union)):
            if array2[j] == union[k]:
                existe = True
        if not existe:
            union += [array2[j]]

    return f'Unión de M y N: {union}'

print(recibir_union(conjuntoM, conjuntoN))
