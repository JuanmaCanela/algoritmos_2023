#Dada una pila de letras determinar cuántas vocales contiene
from pila import Pila
from random import randint

stack_letras = Pila()

#Carga
for i in range(10):
    stack_letras.push(chr(randint(65, 90)))

#Comparar y contar las vocales
contador_vocales = 0
while stack_letras.size() > 0:
    valor = stack_letras.pop()
    if valor in ['A', 'E', 'I', 'O', 'U']:
        contador_vocales += 1

#Mostrar la cantidad de vocales
print(f'Hay {contador_vocales} vocales')