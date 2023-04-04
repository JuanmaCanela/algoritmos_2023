#Implementar una función que calcule la suma de todos los números enteros comprendidos entre cero y un número entero positivo dado

def suma(numero):
    '''Resuelve la suma de todos los números comprendidos entre cero y el número dado'''
    if numero == 0:
        return numero
    else:
        return numero + suma(numero-1)