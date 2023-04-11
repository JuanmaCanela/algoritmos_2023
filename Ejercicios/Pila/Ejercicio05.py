#Determinar si una cadena de caracteres es un palíndromo

from pila import Pila

pila1 = Pila()
pila2 = Pila()
pila3 = Pila()

#Carga
palabra = input('Ingrese un palabra:')
for letra in palabra:
    pila1.push(letra)

#Repartimos la palabra en dos pilas auxiliares
while pila1.size() > 0:
    valor = pila1.pop()
    pila2.push(valor)
    pila3.push(valor)

#Devolvemos los valores a la pila principal
while pila3.size() > 0:
    pila1.push(pila3.pop())

#Comparamos las pilas
while pila1.size() > 0 and pila1.on_top() == pila2.on_top():
    pila1.pop()
    pila2.pop()

#Mostramos si la palabra es o no palindromo
if pila1.size() == 0:
    print('Es palindromo')
else:
    print('No es palindromo')