def ingresar_datos():
    lista_producto1 = [''] * 5
    lista_producto2 = [''] * 5

    for i in range(len(lista_producto1)):
        producto1 = int(input(f'Ingresar el {i + 1} producto: '))
        lista_producto1[i] += [producto1]
    for i in range(len(lista_producto2)):
        producto2 = int(input(f'Ingresar el {i + 1} producto: '))
        lista_producto2[i] += [producto2]

        
    return lista_producto1, lista_producto2

def productos_comun(user1, user2):
    producto = []
    for i in range(len(user1)):
        for j in range(len(user2)):
            if user1[i] == user2[j]:
                producto += [user1[1]]
    return user1[i]

def productos_exclusivos(user1, user2):
    exclusivo1 = []
    exclusivo2 = []
    for i in range(len(user1)):
        for j in range(len(user2)):
            if user1[i] != user2[j]:
                exclusivo1 += [user1[i]]
            elif user2 [j] != user1 [i]:
                exclusivo2 += [user2[j]]
    return exclusivo1, exclusivo2   

def catalogo_total(user1, user2):
    total = []
    for i in range(len(user1)):
        for j in range(len(user2)):
            total += [user1[i]]
            total += [user2[j]]
    return total

def recomendacion():
    return 'Estamos en mantenimiento!'