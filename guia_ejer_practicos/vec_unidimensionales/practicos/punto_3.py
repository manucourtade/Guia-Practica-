# Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números. 
def lista_enteros(vec_int):
    suma_int = 0
    for i in range(len(vec_int)):
        suma_int += vec_int[i]
    return suma_int / len(vec_int)

print(lista_enteros([10, 20, 30, 456]))
