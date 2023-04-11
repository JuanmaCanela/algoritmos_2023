#Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden números pares

from pila import Pila
from random import randint

stack = Pila()
stack_aux = Pila()

#Carga
for i in range(10):
    valor = randint(1, 11)
    print('Numeros:', valor)
    stack.push(valor)

#Evaluacion de pares o impares
while stack.size() > 0:
    valor = stack.pop()
    if valor % 2 == 0:
         stack_aux.push(valor)

#Retornar valores a la pila principal
while stack_aux.size() > 0:
    stack.push(stack_aux.pop())

#Mostrar la pila solo con numeros pares
while stack.size() > 0:
    print(stack.pop())