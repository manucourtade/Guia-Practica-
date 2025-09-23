# Crear una función intercalar_vectores que reciba dos vectores de números enteros ordenados en orden ascendente, 
# y devuelva un único vector también ordenado. 
# La función debe tener un parámetro opcional descendente para que el vector resultante esté en orden descendente.
from punto_1 import ordenar_array


def intercalar_vectores(vec1, vec2, descendente=False):
    vec1_copy = ordenar_array(vec1)        
    vec2_copy = ordenar_array(vec2)          

    print("Vec1 ordenado:", vec1_copy)
    print("Vec2 ordenado:", vec2_copy)

    vec3 = vec1_copy + vec2_copy
    vec3_sort = ordenar_array(vec3, descendente)

    if descendente:
        print("VECTOR RESULTANTE DESCENDENTE")
    else:
        print("VECTOR RESULTANTE ASCENDENTE")
    print(vec3_sort)


# Ejemplo de uso
array1 = [4, 5, 3, 2, 1, 7]
array2 = [12, 54, 32, 67, 12]

intercalar_vectores(array1, array2)         
#intercalar_vectores(array1, array2, True)    

