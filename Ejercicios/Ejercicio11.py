#Desarrollar un algoritmo que invierta un número entero sin convertirlo a cadena

def InvertirNum(numero):
    '''Invierte un numero dado'''
    if (numero // 10 == 0):
        return numero
    else:
        return (numero % 10) * 10 ** len(str(numero//10)) + InvertirNum(numero // 10)