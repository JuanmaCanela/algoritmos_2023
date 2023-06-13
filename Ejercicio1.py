#Desarrollar una función recursiva que permita contar cuantas veces aparece una determinada palabra, en un vector de palabras.

lista_palabras=["casa", "auto", "pelota", "clase", "aula", "casa", "perro", "gato", "casa", "pelota"]

def contar_palabra(vector, palabra, indice=0):
    if indice >= len(vector):
        return 0
    if vector[indice] == palabra:
        return 1 + contar_palabra(vector, palabra, indice + 1)
    else:
        return contar_palabra(vector, palabra, indice + 1)
    
print(contar_palabra(lista_palabras, "casa"))