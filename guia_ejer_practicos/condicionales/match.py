
# MATCH

estacion = input('Ingrese la estacion del año: ').lower()
destino = input('Ingrese el destino (Bariloche, Cataratas, Mar del Plata): ').lower()

match estacion:
    case 'invierno':
        if destino != 'bariloche':
            print('No se viaja')
        else:
            print('Se viaja')

    case 'verano':
        if destino == 'bariloche':
            print('No se viaja')
        else:
            print('Se viaja')

    case 'otoño':
        print('Se viaja')

    case 'primavera':
        if destino == 'bariloche':
            print('No se viaja')
        else:
            print('Se viaja')
    case _:
        print('Ingrese la opcion correcta!')
