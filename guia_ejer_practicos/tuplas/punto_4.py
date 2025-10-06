# Tuplas anidadas
# Crear una tupla llamada estudiante con el siguiente formato: estudiante = ('Lucía', 'Martínez', (8.5, 9.0,7.5))
# Mostrar:
# ● El nombre completo del estudiante.
# ● El promedio de las notas almacenadas en la tupla anidada.

estudiante = ('Lucía', 'Martínez', (8.5, 9.0,7.5))

nombre, apellido, notas = estudiante

print(f'Nombre completo: {nombre} {apellido}')
suma = 0
for i in range(len(notas)):
    suma += notas[i] 
promedio = suma / 3

print(f'Promedio del estudiante: {promedio:.2f}')
