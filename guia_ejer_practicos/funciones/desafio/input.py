from validate import validate_number as vn
from validate import validate_lenght as vl

def get_int(mensaje:str, mensaje_error:str, minimo:int , maximo:int, reintentos:int) -> int|None:
    print(mensaje)
    while reintentos > 0:
        num_int = int(input('Ingrese un número: '))
        if not vn(num_int, minimo, maximo):
            print(mensaje_error)
            reintentos -= 1
            print(f'Te quedan {reintentos} intentos')
        else:
            return num_int
    print('Se quedó sin intentos!')
    return None

def get_float(mensaje:str, mensaje_error:str, minimo:float, maximo:float, reintentos:int) -> float|None:
    print(mensaje)
    while reintentos > 0:
        num_float = float(input('Ingrese un número: '))
        if not vn(num_float, minimo, maximo):
            print(mensaje_error)
            reintentos -= 1
            print(f'Te quedan {reintentos} intentos')
        else:
            return num_float
    print('Se quedó sin intentos!')
    return None

def get_string(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int) -> str|None:
    print(mensaje)
    while reintentos > 0:
        texto = input('Ingrese un texto: ')
        longitud = len(texto)
        if not vl(texto, minimo, maximo):  
            print(mensaje_error)
            reintentos -= 1
            print(f'Te quedan {reintentos} intentos')
        else:
            return longitud, texto  
    print('Se quedó sin intentos!')
    


# Ejemplo de uso

num_int = get_int('Aqui vas ingresar numeros enteros!', 'Tienes que ingresar entre 35 y 50 números enteros!', 35, 50, 3)
num_float = get_float('Aqui vaas ingresar numeros flotantes!', 
                        'Tienes que ingresar entre 123.4 y 130.6 números flotantes!', 123.4, 130.6, 3)
longitud, texto = get_string('Aqui vas a ingresar una cadena!', 'Tienes que ingresar entre 12 y 35 caracteres.', 12, 35, 3)

def resumen(num_int:int, num_float:float, texto: str, longitud: int):
    print(f'''
    RESULTADOS DE LA FUNCION:
    get_int: {num_int}
    get_float: {num_float}
    get_string: {texto} tiene {longitud} letras''')

resumen(num_int, num_float, texto, longitud)
