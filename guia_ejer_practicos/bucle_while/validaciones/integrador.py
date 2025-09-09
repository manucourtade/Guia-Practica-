'''
Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.
 
Los datos requeridos son:
Apellido
Edad, entre 18 y 90 años inclusive.
Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.
'''
apellido = input('Ingrese su apellido: ')
edad = int(input('Ingrese su edad: '))
estado_civil = input('“Soltero”, ”Casado”, “Divorciado” o “Viudo”: ').lower()
n_legajo =int(input('Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda: '))

while edad < 18 or edad > 90:
    print('Edad entre 18 y 90 años inclusive.')
    edad = int(input('Ingrese su edad: '))

while estado_civil != 'soltero' and estado_civil != 'casado' and estado_civil != 'divorciado' and estado_civil != 'viudo':
    print('Tienes que ingresar: “Soltero”, ”Casado”, “Divorciado” o “Viudo”')
    estado_civil = input('“Soltero”, ”Casado”, “Divorciado” o “Viudo”: ').lower()

while  n_legajo < 1000:
    print('valor numérico de 4 cifras, sin ceros a la izquierda. ej 1111')
    n_legajo =int(input('Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda: '))

print(f'''
Apellido: {apellido}
Edad: {edad}
Estado Civil: {estado_civil}
N° Legajo: {n_legajo}''')