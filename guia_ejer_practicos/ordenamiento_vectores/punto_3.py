# Crear una función que reciba como parámetro un vector de números enteros.
#  La función debe mostrar los números negativos de forma decreciente y luego los positivos de forma creciente. 
#Nota: solo se puede usar un vector, y se debe utilizar la menor cantidad de estructuras repetitivas.

def vec_int(vec):
    n = len(vec)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if vec[j] > vec[j + 1]:
                vec[j], vec[j + 1] = vec[j + 1], vec[j]
    k = 0
    while k < n and vec[k] < 0:
        k += 1

    a, b = 0, k - 1
    while a < b:
        vec[a], vec[b] = vec[b], vec[a]
        a += 1
        b -= 1

    print(vec)

mi_vec = [1545, -1221, -43, 2, 1, 4, -8, 3, 12, -76, 123]
vec_int(mi_vec)

