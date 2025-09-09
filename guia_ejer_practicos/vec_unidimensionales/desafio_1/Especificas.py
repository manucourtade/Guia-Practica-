def cantidad_positivos_negativos(lista_enteros):
    contador_pos = 0
    contador_neg = 0
    for i in range(len(lista_enteros)):
        if lista_enteros[i] > 0:
            contador_pos += 1
        else:
            contador_neg += 1
    print(f'Cantidad de numeros positivos: {contador_pos}')
    print(f'Cantidad de numeros negativos: {contador_neg}')
        
def mayor_numero_impar(lista_enteros):
    valor_max = 0
    for i in range(len(lista_enteros)):
        if not lista_enteros[i] % 2 == 0:
            if lista_enteros[i] > valor_max:
                valor_max = lista_enteros[i]
    return f'Numero mayor impar {valor_max}'

