#Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
#su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
#necesarias para resolver las siguientes actividades:

#a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
#b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

class PersonajeMCU:
    def __init__(self, nombre, peliculas):
        self.nombre = nombre
        self.peliculas = peliculas


def determinar_posicion_rocket_groot(pila_personajes):
    posicion = None
    contador = 1
    for personaje in pila_personajes:
        if personaje.nombre == "Rocket Raccoon" or personaje.nombre == "Groot":
            posicion = contador
            break
        contador += 1
    return posicion


def personajes_mas_de_5_peliculas(pila_personajes):
    personajes = []
    for personaje in pila_personajes:
        if personaje.peliculas > 5:
            personajes.append((personaje.nombre, personaje.peliculas))
    return personajes


def participacion_viuda_negra(pila_personajes):
    participacion = 0
    for personaje in pila_personajes:
        if personaje.nombre == "Viuda Negra":
            participacion = personaje.peliculas
            break
    return participacion


def mostrar_personajes_cdg(pila_personajes):
    print("Personajes cuyos nombres empiezan con C, D y G:")
    for personaje in pila_personajes:
        if personaje.nombre[0] in ["C", "D", "G"]:
            print(personaje.nombre)
