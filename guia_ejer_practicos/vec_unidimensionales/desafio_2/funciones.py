

def productos_comun(user1, user2):
    producto = []
    for i in range(len(user1)):
        for j in range(len(user2)):
            if user1[i] == user2[j]:
                producto += [user1[i]]   
    return producto


def productos_exclusivos(user1, user2):
    exclusivo1 = []
    exclusivo2 = []
    
    for i in range(len(user1)):
        encontrado = False
        for j in range(len(user2)):
            if user1[i] == user2[j]:
                encontrado = True
        if not encontrado:
            exclusivo1 += [user1[i]]

    for j in range(len(user2)):
        encontrado = False
        for i in range(len(user1)):
            if user2[j] == user1[i]:
                encontrado = True
        if not encontrado:
            exclusivo2 += [user2[j]]

    return exclusivo1, exclusivo2


def catalogo_total(user1, user2):
    total = []
    for i in range(len(user1)):
        total += [user1[i]]
    
    for j in range(len(user2)):
        total += [user2[j]]
    
    return total

def recomendar(user1, user2):
    exclusivo1, exclusivo2 = productos_exclusivos(user1, user2)

    recomendaciones_user1 = exclusivo2  
    recomendaciones_user2 = exclusivo1  

    return recomendaciones_user1, recomendaciones_user2
