

def validate_number(valor: int|float, minimo: int, maximo: int):
    if minimo <= valor <= maximo:
        return valor
            

def validate_lenght(texto: str, minimo: int, maximo: int) -> bool:
    if minimo <= len(texto) <= maximo:
        longitud = len(texto)
        return longitud

