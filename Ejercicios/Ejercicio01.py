#Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un número dado

def fib(num):
    '''Resuelve la sucesion de Fibonacci para el numero dado'''
    if (num==0) or (num==1):
        return num
    else:
        return fib(num-1) + fib(num-2)