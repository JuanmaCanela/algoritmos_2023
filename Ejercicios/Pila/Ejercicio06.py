#Leer una palabra y visualizarla en forma inversa
from pila import Pila

stack_palabra = Pila()

#Carga
palabra = input('Ingrese una palabra:')
for i in palabra:
    stack_palabra.push(i)

#Inversión
palabra_invertida = ''
while stack_palabra.size() > 0:
    palabra_invertida += stack_palabra.pop()

#Mostrar la palabra invertida
print(palabra_invertida)