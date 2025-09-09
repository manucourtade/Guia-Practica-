import random as rm

numero_random = rm.randrange(1,11)

if numero_random >= 6:
    print(f'Promocion Directa, la nota es {numero_random}')
elif numero_random >= 4:
    print(f'Aprobado, la nota es {numero_random}')
else:
    print(f'Desaprobado, la nota es {numero_random}')