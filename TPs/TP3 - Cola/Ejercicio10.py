#Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone, de las cual se cuenta con la hora de la 
#notificación, la aplicación que la emitió y el mensaje,resolver las siguientes actividades:

#a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
#b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra ‘Python’, si perder datos en la cola;
#c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.

from collections import deque

class Notificacion:
    def __init__(self, hora, aplicacion, mensaje):
        self.hora = hora
        self.aplicacion = aplicacion
        self.mensaje = mensaje

def eliminar_notificaciones_facebook(cola):
    while len(cola) > 0 and cola[0].aplicacion == "Facebook":
        cola.popleft()

def mostrar_notificaciones_twitter_python(cola):
    print("Notificaciones de Twitter con la palabra 'Python':")
    for notificacion in cola:
        if notificacion.aplicacion == "Twitter" and "Python" in notificacion.mensaje:
            print(f"Hora: {notificacion.hora} - Mensaje: {notificacion.mensaje}")

def contar_notificaciones_entre_horas(cola):
    pila_temporal = []
    contador = 0
    while len(cola) > 0:
        notificacion = cola.popleft()
        if "11:43" <= notificacion.hora <= "15:57":
            contador += 1
        pila_temporal.append(notificacion)
    while len(pila_temporal) > 0:
        cola.appendleft(pila_temporal.pop())
    return contador