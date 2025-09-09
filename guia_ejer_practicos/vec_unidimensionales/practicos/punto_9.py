# Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la intersección de los dos arrays.

conjuntoM = ['a', 'c', 'b', 'j', 'f']
conjuntoN = ['l', 'g', 'b', 'e', 'i', 'h']

def recibir_interseccion(array1, array2):
    interseccion = []
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] == array2[j]:
                interseccion += [array1[i]]  
    return f'Intersección de M y N: {interseccion}'

print(recibir_interseccion(conjuntoM, conjuntoN))