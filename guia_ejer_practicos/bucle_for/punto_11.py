# Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. 
# Informar cuántos números primos se encontraron.

num = int(input('Ingrese un numero: '))
contador_primos = 0  # cuenta los primos encontrados

for n in range(2, num + 1):  # arrancamos en 2 porque 1 no es primo
    es_primo = True
    for i in range(2, n):
        if n % i == 0:   # si tiene un divisor, no es primo
            es_primo = False
            break
    if es_primo:
        print(n)  # mostramos el primo
        contador_primos += 1

print(f'Se encontraron {contador_primos} numeros primos')
