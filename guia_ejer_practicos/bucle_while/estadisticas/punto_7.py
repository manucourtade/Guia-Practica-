'''Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
Calcular la suma de los números positivos y el producto de los negativos.'''
contador = 0
suma_pos = 0
prod_neg = 1
while True:
    contador += 1
    num = int(input(f'Ingrese el numero {contador}: '))
    
    fin = input('Desea terminar? (s/n)?: ').lower()
    if num > 0:
        suma_pos += num
    elif num < 0:
        prod_neg *= num
    
    if fin == 's':
        break

print(f'Suma acumulada de positivos: {suma_pos}, producto acumulados de negativos: {prod_neg}, introdujo {contador} numeros')
    