# Crear una función llamada ordenar_array que reciba como parámetro un array de números enteros y lo ordene de forma ascendente. 
# La función debe implementar como algoritmo de ordenamiento el método de la burbuja. 
# Además, como parámetro opcional debe recibir un booleano (que por default está en False), 
# que en caso de ser True ordena el vector en forma descendente.

def ordenar_array(array, b = False):
    tam = len(array)
    if b == False:
        for i in range(tam - 1):
            for j in range(tam - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        #print('Vector ordenado de forma ascendente')
        #print(array)
    else:
        for i in range(tam - 1):
            for j in range(tam - i - 1):
                if array[j] < array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        #print('Vector ordenado de forma descedente')
        #print(array)
    return array
#mi_lista = [2, 5, 3, 1, 6, 78]
#ordenar_array(mi_lista)
