#Dada una lista con nombres de personajes de la saga de Avengers ordenados por nombre del superhéroes, de los cuales se conoce:
#nombre del superhéroe, nombre del personaje (puede ser vacio), grupo al que (perteneces puede ser vacio), año de aparición, por ejemplo 
#(Star Lord – Peter Quill – Guardianes de la galaxia - 1976). Resolver las siguientes tareas:

#a. Determinar si “Capitana Marvel” está en la lista y mostrar su nombre de personaje;
#b. Almacenar los superhéroes que pertenezcan al grupo “Guardianes de la galaxia” en una cola e indicar cuantos son.
#c. Mostrar de manera descendente los superhéroes que pertenecen al grupo “Los cuatro fantásticos” y “Guardoanes de la galaxia”.
#d. Listar los superhéroes que tengan nombre de personajes cuyo año de aparición sea posterior a 1960.
#e. Hemos detectado que la superhéroe “Black Widow” está mal cargada por un error de tipeo, figura como “Vlanck Widow”,
#modifique dicho superhéroe para solucionar este problema.
#f. Dada una lista auxiliar con los siguientes personajes (‘Black Cat’, ‘Hulk’, ‘Rocket Racoonn’, ‘Loki’, complete el resto de la información), 
#agregarlos a la lista principal en el caso de no estar cargados.
#g. Mostrar todos los personajes que comienzan con C, P o S.
#h. Cargue al menos 20 superheroes a la lista.

# Lista principal de personajes de Avengers
avengers = [
    ["Star Lord", "Peter Quill", "Guardianes de la galaxia", 1976],
    ["Capitán América", "Steve Rogers", "Los Vengadores", 1941],
    ["Capitana Marvel", "Carol Danvers", "", 1995],
    ["Iron Man", "Tony Stark", "Los Vengadores", 1963],
    ["Thor", "", "Los Vengadores", 1962],
    ["Viuda Negra", "Vlanck Widow", "Los Vengadores", 1964],
    ["Hulk", "", "", 1962],
    ["Sr. Fantástico", "Reed Richards", "Los cuatro fantásticos", 1961],
    ["Mujer Invisible", "Susan Sue Storm", "Los cuatro fantásticos", 1961],
    ["Antorcha Humana", "Johnny Storm", "Los cuatro fantásticos", 1961],
    ["La Mole", "Ben Grimm", "Los cuatro fantásticos", 1961],
]

#a. Determinar si "Capitana Marvel" está en la lista y mostrar su nombre de personaje
capitana_marvel = next((personaje[1] for personaje in avengers if personaje[0] == "Capitana Marvel"), None)
if capitana_marvel:
    print("Capitana Marvel está en la lista.")
    print("Nombre de personaje:", capitana_marvel)
else:
    print("Capitana Marvel no está en la lista.")

#b. Almacenar los superhéroes que pertenezcan al grupo "Guardianes de la galaxia" en una cola e indicar cuántos son
from collections import deque

guardianes_de_la_galaxia = deque(personaje[0] for personaje in avengers if personaje[2] == "Guardianes de la galaxia")
print("Superhéroes en el grupo Guardianes de la galaxia:", len(guardianes_de_la_galaxia))

#c. Mostrar de manera descendente los superhéroes que pertenecen al grupo "Los cuatro fantásticos" y "Guardianes de la galaxia"
cuatro_fantasticos = [personaje[0] for personaje in avengers if personaje[2] == "Los cuatro fantásticos"]
guardianes_galaxia = [personaje[0] for personaje in avengers if personaje[2] == "Guardianes de la galaxia"]
cuatro_fantasticos.reverse()
guardianes_galaxia.reverse()
print("Superhéroes en el grupo Los cuatro fantásticos (en orden descendente):", cuatro_fantasticos)
print("Superhéroes en el grupo Guardianes de la galaxia (en orden descendente):", guardianes_galaxia)

#d. Listar los superhéroes que tengan nombre de personajes cuyo año de aparición sea posterior a 1960
superheroes_post_1960 = [personaje[0] for personaje in avengers if personaje[1] and personaje[3] > 1960]
print("Superhéroes con nombre de personaje posterior a 1960:", superheroes_post_1960)

#e. Corregir el nombre "Vlanck Widow" por "Black Widow"
for personaje in avengers:
    if personaje[1] == "Vlanck Widow":
        personaje[1] = "Black Widow"

#f. Agregar los personajes de la lista auxiliar a la lista principal si no están cargados
lista_auxiliar = [
    ["Black Cat", "", "", 1979],
    ["Hulk", "", "Los Vengadores", 1962],
    ["Rocket Racoonn", "", "Guardianes de la galaxia", 2008],
    ["Loki", "", "", 1962]
]

for personaje_auxiliar in lista_auxiliar:
    nombre_personaje = personaje_auxiliar[0]
    if not any(personaje[0] == nombre_personaje for personaje in avengers):
        avengers.append(personaje_auxiliar)

#g. Mostrar todos los personajes que comienzan con C, P o S
personajes_cps = [personaje[0] for personaje in avengers if personaje[0][0] in ["C", "P", "S"]]
print("Personajes que comienzan con C, P o S:", personajes_cps)

# h. Cargar al menos 20 superhéroes a la lista (en la lista ya hay 14)
nuevo_personaje1 = ["Spider-Man", "Peter Parker", "", 1962]
avengers.append(nuevo_personaje1)

nuevo_personaje2 = ["Doctor Strange", "", "", 1963]
avengers.append(nuevo_personaje2)

nuevo_personaje3 = ["Black Panther", "T'Challa", "", 1966]
avengers.append(nuevo_personaje3)

nuevo_personaje4 = ["Superman", "Clark Kent", "DC", 1978]
avengers.append(nuevo_personaje4)

nuevo_personaje5 = ["Aquaman", "Arthur Curry", "DC", 1941]
avengers.append(nuevo_personaje5)

nuevo_personaje6 = ["Batman", "Bruce Wayne", "DC", 1939]
avengers.append(nuevo_personaje6)

print("Cantidad de personajes en la lista:", len(avengers))