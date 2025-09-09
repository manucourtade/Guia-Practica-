# Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.


while True:
    clave = input('Ingrese una clave: ')
    if clave == 'alfajuancri123':
        print('Clave correcta, acceso permitido')
        break
    else:
        print('Incorrecta intente de nuevo!')
    