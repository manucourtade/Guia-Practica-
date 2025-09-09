# Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:
#Una lista de nombres (lista_nombres).
#Un nombre a buscar en la lista (nombre_antiguo).
#Un nombre de reemplazo (nombre_nuevo).
#La función debe realizar las siguientes acciones:
#Reemplazar todas las apariciones de nombre_antiguo en lista_nombres por nombre_nuevo.
#Retornar la cantidad total de reemplazos realizados.
vec_nombres = ["Manu", "Jose", "Martin"]
name_old = "Jose"
name_new = "Paulo" 


def reemplazar_nombres(lista_nombres, nombre_antiguo, nombre_nuevo):
    reemplazos = 0
    for i in range(len(lista_nombres)):
        if nombre_antiguo == lista_nombres[i]:
            lista_nombres[i] = nombre_nuevo
            reemplazos += 1
    return reemplazos  # retorna solo la cantidad

# Llamada a la función
cantidad = reemplazar_nombres(vec_nombres, name_old, name_new)

print("Lista modificada:", vec_nombres)
print("Cantidad de reemplazos:", cantidad)

    
