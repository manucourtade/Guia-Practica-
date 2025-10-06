# Función que retorna tupla
# Crear una función llamada datos_usuario() que pida al usuario su nombre, edad y país por teclado, y
# retorne esa información como una tupla. Mostrar la tupla resultante desde el programa principal.

def datos_usuario():
    nombre = input('Ingrese su nombre: ')
    edad = int(input('Ingrese su edad: '))
    pais = input('Ingrese su pais: ')
    return nombre, edad, pais

print('TUPLA RESULTANTE')
print(datos_usuario())