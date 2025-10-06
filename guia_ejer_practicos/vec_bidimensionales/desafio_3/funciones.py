

def definir_matriz():
    matriz = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    
    for i in range(len(matriz)):
        print(f'Fila {i + 1}')
        for j in range(len(matriz[i])):
            nums = int(input(f'Ingrese el {j + 1} entero: '))
            matriz[i][j]= nums
    return matriz

mi_matriz = definir_matriz()

def verificar_secuencia(matriz: list):
    ocurrencias = 0
    for fila in matriz:
        for j in range(len(fila) - 2):  # hasta -2 para poder mirar j+2
            if (fila[j] % 2 == 0 and fila[j+1] % 2 == 0 and fila[j+2] % 2 == 0):
                if fila[j] - fila[j+1] == 2 and fila[j+1] - fila[j+2] == 2:
                    ocurrencias += 1
    return ocurrencias


def cant_ocurrencias(matriz):
    cant = verificar_secuencia(matriz)
    if cant == 0:
        return '❌ No existen números consecutivos pares'
    elif cant == 1:
        return '✅ Solo se encontró una ocurrencia'
    else:
        return f'✅ Existen números consecutivos pares, hay {cant} ocurrencias'
    
print(cant_ocurrencias(mi_matriz))
