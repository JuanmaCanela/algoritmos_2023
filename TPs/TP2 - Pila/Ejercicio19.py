#Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de estreno, 
#desarrollar las funciones necesarias para resolver las siguientes actividades:

#a. mostrar los nombre películas estrenadas en el año 2014;
#b. indicar cuántas películas se estrenaron en el año 2018;
#c. mostrar las películas de Marvel Studios estrenadas en el año 2016.

class Pelicula:
    def __init__(self, titulo, estudio, año_estreno):
        self.titulo = titulo
        self.estudio = estudio
        self.año_estreno = año_estreno


def mostrar_peliculas_2014(pila_peliculas):
    print("Películas estrenadas en 2014:")
    for pelicula in pila_peliculas:
        if pelicula.año_estreno == 2014:
            print(pelicula.titulo)


def contar_peliculas_2018(pila_peliculas):
    cont = 0
    for pelicula in pila_peliculas:
        if pelicula.año_estreno == 2018:
            cont += 1
    return cont


def mostrar_peliculas_marvel_2016(pila_peliculas):
    print("Películas de Marvel Studios estrenadas en 2016:")
    for pelicula in pila_peliculas:
        if pelicula.estudio == "Marvel Studios" and pelicula.año_estreno == 2016:
            print(pelicula.titulo)
