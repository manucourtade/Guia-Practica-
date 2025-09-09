# Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.
contador = 3

while contador > 0:

    contador -= 1

    clave = input('Ingrese una clave: ')

    if clave == 'alfajuancri123':
        print('Clave correcta, acceso permitido')
        break
    elif contador == 0:
        print('Vuelva a intentar mas tarde, se quedo sin intentos!')
    else:
        print(f'Incorrecta intente de nuevo! le quedan {contador} intentos!')