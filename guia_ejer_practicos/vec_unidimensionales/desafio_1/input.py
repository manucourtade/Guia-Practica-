import Arrays_Generales as ag
import Especificas as es



def operaciones_conjuntos():
    mi_lista = None

    while True:
        print("1. Ingresar números")
        print("Menú:")
        print("2. Cantidad de positivos y negativos")
        print("3. Suma de números pares")
        print("4. Mayor número impar")
        print("5. Listar todos los números ingresados")
        print("6. Listar números pares")
        print("7. Listar números en posiciones impares")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")
            
        if opcion == '1':
            mi_lista = ag.ingresar_datos()
            print("Tu lista:", mi_lista)

        elif opcion in ['2','3','4','5','6','7']:
            if mi_lista is None:
                print("Primero debe ingresar los números (opción 1).")
            else:
                if opcion == '2':
                    es.cantidad_positivos_negativos(mi_lista)
                elif opcion == '3':
                    suma_pares = ag.suma_pares(mi_lista)
                    print(suma_pares)
                elif opcion == '4':
                    max_impar = es.mayor_numero_impar(mi_lista)
                    print(max_impar)
                elif opcion == '5':
                    ag.listar_numeros_ingresados(mi_lista)
                elif opcion == '6':
                    ag.listar_numeros_pares(mi_lista)
                elif opcion == '7':
                    ag.listar_numeros_posiciones_impares(mi_lista)
            
        elif opcion == '8':
            print("Hasta luego!")
            break
        else:
            print("Opción inválida. Ingrese un número del 1 al 8.")

operaciones_conjuntos()
