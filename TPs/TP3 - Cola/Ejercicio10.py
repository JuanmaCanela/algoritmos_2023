#Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone, de las cual se cuenta con la hora de la notificación, 
#la aplicación que la emitió y el mensaje,resolver las siguientes actividades:

#a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
#b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra ‘Python’, si perder datos en la cola;
#c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.

from queue import Queue

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

#Cola de notificaciones
cola_notificaciones = Queue()


#a. Función para eliminar las notificaciones de Facebook de la cola
def eliminar_notificaciones_facebook(cola):
    cantidad_eliminadas = 0
    tamano_inicial = cola.qsize()

    for _ in range(tamano_inicial):
        notificacion = cola.get()

        if notificacion[1] != "Facebook":
            cola.put(notificacion)
        else:
            cantidad_eliminadas += 1

    return cantidad_eliminadas

#b. Función para mostrar las notificaciones de Twitter que contengan la palabra 'Python'
def mostrar_notificaciones_twitter_python(cola):
    cantidad_mostradas = 0
    tamano_inicial = cola.qsize()

    for _ in range(tamano_inicial):
        notificacion = cola.get()

        if notificacion[1] == "Twitter" and "Python" in notificacion[2]:
            print("Hora:", notificacion[0])
            print("Mensaje:", notificacion[2])
            print("-----")
            cantidad_mostradas += 1

        cola.put(notificacion)

    return cantidad_mostradas

#c. Función para almacenar temporalmente las notificaciones entre las 11:43 y las 15:57
def almacenar_notificaciones_temporalmente(cola):
    pila_temporal = Stack()
    cantidad_almacenadas = 0

    while not cola.empty():
        notificacion = cola.get()
        hora = notificacion[0]

        if "11:43" <= hora <= "15:57":
            pila_temporal.push(notificacion)
            cantidad_almacenadas += 1
        else:
            cola.put(notificacion)

    return cantidad_almacenadas

#Notificaciones para probar el programa
cola_notificaciones.put(("11:30", "Facebook", "Mensaje 1"))
cola_notificaciones.put(("12:15", "Twitter", "Mensaje 2 con Python"))
cola_notificaciones.put(("14:20", "Facebook", "Mensaje 3"))
cola_notificaciones.put(("15:50", "Twitter", "Mensaje 4 con Python"))
cola_notificaciones.put(("16:30", "Twitter", "Mensaje 5 con Python"))

#a. Eliminar las notificaciones de Facebook de la cola
cantidad_eliminadas = eliminar_notificaciones_facebook(cola_notificaciones)
print("Se eliminaron", cantidad_eliminadas, "notificaciones de Facebook")

#b. Mostrar las notificaciones de Twitter que contengan la palabra 'Python'
cantidad_mostradas = mostrar_notificaciones_twitter_python(cola_notificaciones)
print("Se mostraron", cantidad_mostradas, "notificaciones de Twitter que contienen 'Python'")

#c. Almacenar temporalmente las notificaciones entre las 11:43 y las 15:57
cantidad_almacenadas = almacenar_notificaciones_temporalmente(cola_notificaciones)
print("Se almacenaron temporalmente", cantidad_almacenadas, "notificaciones")