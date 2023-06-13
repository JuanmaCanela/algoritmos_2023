#Se recuperó la bitácora de la nave del cazarrecompensas Boba Fett, la cual se almacenaban en una pila en cada misión de caza que emprendió 
#(con la siguiente información planeta visitado, a quien capturado, costo de la recompensa), resolver las siguientes actividades:

#a. Mostrar los planetas visitados en el orden hizo las misiones.
#b. Determinar cuántos créditos galácticos recaudo en total.
#c. Determinar el número de la misión en que capturo a Han Solo y en que planeta fue, suponga que dicha misión está cargada.


class Bitacora_BobaFett:
    def __init__(self, planeta, capturado, recompensa):
        self.planeta = planeta
        self.capturado = capturado
        self.recompensa = recompensa

pila_bitacoras = []

bitacora1 = Bitacora_BobaFett("Jupiter", "Chewbacca", 500)
pila_bitacoras.append(bitacora1)

bitacora2 = Bitacora_BobaFett("Plutón", "Obi-Wan Kenobi", 1000)
pila_bitacoras.append(bitacora2)

bitacora3 = Bitacora_BobaFett("Urano", "Han Solo", 1500)
pila_bitacoras.append(bitacora3)

bitacora4 = Bitacora_BobaFett("Neptuno", "C-3PO", 2000)
pila_bitacoras.append(bitacora4)

#a. Mostrar los planetas visitados en el orden hizo las misiones.
def mostrar_planetas_visitados(pila_bitacoras):
    print("Planetas visitados en orden de misiones:")
    for bitacora in pila_bitacoras:
        print(bitacora.planeta)

#b. Determinar cuántos créditos galácticos recaudo en total.
def calcular_creditos_recaudados(pila_bitacoras):
    total_creditos = 0
    for bitacora in pila_bitacoras:
        total_creditos += bitacora.recompensa
    return total_creditos

#c. Determinar el número de la misión en que capturo a Han Solo y en que planeta fue, suponga que dicha misión está cargada.
def buscar_mision_han_solo(pila_bitacoras):
    numero_mision = 0
    planeta = ""
    for bitacora in pila_bitacoras:
        numero_mision += 1
        if bitacora.capturado == "Han Solo":
            planeta = bitacora.planeta
            break
    return numero_mision, planeta

print(mostrar_planetas_visitados(pila_bitacoras))
print(calcular_creditos_recaudados(pila_bitacoras))
print(buscar_mision_han_solo(pila_bitacoras))