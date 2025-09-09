def ingresar_datos():
    lista_enteros = [0] * 10

    for i in range(len(lista_enteros)):
        num = int(input(f'Ingresar el {i + 1} numero: '))
        if -1000 <= num <= 1000:
            lista_enteros[i] = num
        
    return lista_enteros

def suma_pares(lista_enteros):
    sumas = 0
    for i in range(len(lista_enteros)):
        if lista_enteros[i] % 2 == 0:
            sumas += lista_enteros[i]
    return f'Sumatoria de numeros pares: {sumas}'

def listar_numeros_ingresados(lista_enteros):
    for i in range(len(lista_enteros)):
        print(lista_enteros[i])
    

def listar_numeros_pares(lista_enteros):
    for i in range(len(lista_enteros)):
        if lista_enteros[i] % 2 == 0:
            print(lista_enteros[i])

def listar_numeros_posiciones_impares(lista_enteros):
    for i in range(len(lista_enteros)):
        if not i % 2 == 0:
            print(f'{lista_enteros[i]} se encuentra en la posicion {i}')