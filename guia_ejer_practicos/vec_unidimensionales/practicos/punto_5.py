# Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.
def producto_elementos(vec_prod):
    producto = 1
    for i in range(len(vec_prod)):
        producto *= vec_prod[i]
    return f'Producto de todos los elementos {producto:.0f}'

print(producto_elementos([10, 20, 30, 456]))
