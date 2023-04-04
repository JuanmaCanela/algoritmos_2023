#Determinar el número de ocurrencias de un determinado elemento en una pila

from pila import Pila
from random import randint

stack = Pila()

#Carga de caracteres
for i in range(20):
    valor = chr(randint(33, 126))
    print('Caracteres:', valor)
    stack.push(valor)

#Elegir el caracter a ver si se repite
buscado = input('Ingrese un caracter:')

#Comparar y contar si se repite
contador_repeticiones = 0
while stack.size() > 0:
    valor = stack.pop()
    if valor == buscado:
        contador_repeticiones += 1

#Mostrar cantidad de repeticiones
print(f'El caracter buscado se repite {contador_repeticiones} veces')