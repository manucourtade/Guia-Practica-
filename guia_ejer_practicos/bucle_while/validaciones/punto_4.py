# Solicitarle al usuario el ingreso de un color. Validar que el mismo sea Rojo, Verde o Azul.

color = input('Ingrese un color: ').lower()

while color != 'rojo' and color != 'verde' and color != 'azul':
    print(f' No tenemos registado {color}, Intente de nuevo')
    color = input('Ingrese un color: ').lower()

print(f'Ha ingresado el color {color}')