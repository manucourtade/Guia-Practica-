# Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.
from punto_1 import num_entero 
from punto_2 import num_flotante 
from punto_3 import pedir_cadena 

def especializar():
    entero_val = num_entero()
    while entero_val != 11:
        print('Ingrese otro entero')
        entero_val = num_entero()

    
    flotante_val = num_flotante()
    while not(0.5 <= flotante_val <= 10.5):
        print('Ingrese otro flotante')
        flotante_val = num_flotante()

    cadena_val = pedir_cadena()
    while cadena_val != 'Hola' and cadena_val != 'Chau' and cadena_val != 'ca':
        print('Ingrese otra cadena')
        cadena_val = pedir_cadena() 
    
    return entero_val, flotante_val, cadena_val

resultado = especializar()
print("Valores ingresados:", resultado)
