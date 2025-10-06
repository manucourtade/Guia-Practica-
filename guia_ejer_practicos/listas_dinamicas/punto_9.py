# Vaciar una lista
# Mostrá cómo vaciar completamente una lista usando clear().

estudiante = ["María", "Gómez", 32456]

sublista = [10, 8, 7]
estudiante.append(sublista)


estudiante[3].append(9.5)

estudiante2 = ['Manuel', 'Courtade', 32152, [9, 10, 8]]
lista_estudiantes = []

lista_estudiantes.extend([estudiante, estudiante2])
print(lista_estudiantes)

lista_estudiantes.clear()
print('LISTA VACIA')
print(lista_estudiantes)