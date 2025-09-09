# Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.
def lista_enteros(vec_int):
    suma_int = 0
    for i in range(len(vec_int)):
        if vec_int[i] > 0:
            suma_int += vec_int[i]
        else:
            return 'Solamente numeros positivos!'
    return suma_int / len(vec_int)
        
    
    
    
    
print(lista_enteros([-10, 20, 30, 456]))
