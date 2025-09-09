# Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
def max_nums(n1:float, n2:float, n3:float) -> float:
    if n2 <= n1 >= n3:
        return n1
    elif n1 <= n2 >= n3:
        return n2
    else:
        return n3

n1:float = float(input('Ingrese el primer numero: '))
n2:float = float(input('Ingrese el segundo numero: '))
n3:float = float(input('Ingrese el tercero numero: '))

print('Num mas grande:',max_nums(n1,n2,n3))