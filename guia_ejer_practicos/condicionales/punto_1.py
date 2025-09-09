#Condicionales

#IF - ELSE - ELIF

altura = float(input('Ingrese la altura del basquetbolista: '))

if altura < 160:
    print('Base')
elif altura <= 179:
    print('Escolta')
elif altura <= 199:
    print('Alero')
else:
    print('Ala-Pivot o Pivot')
