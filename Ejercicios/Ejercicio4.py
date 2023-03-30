#Implementar una función para calcular la potencia dado dos números enteros, el primero representa la base y segundo el exponente

def potencia(base, exponente):
    '''Resuelve la potencia tomando el primer número ingresado como base y el segundo como exponente'''
    if exponente == 1:
        return base
    else:
        return base * potencia(base, exponente-1)