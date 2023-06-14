#Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente criterio 
#(1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la siguiente situación:

#a. cargue tres documentos de empleados (cada documento se representa solamente con un nombre).
#b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
#c. cargue dos documentos del staff de TI.
#d. cargue un documento del gerente.
#e. imprima los dos primeros documentos de la cola.
#f. cargue dos documentos de empleados y uno de gerente.
#g. imprima todos los documentos de la cola de impresión.

from queue import PriorityQueue

# Crear una cola de prioridad
cola_impresion = PriorityQueue()

cola_impresion.put((1, "Documento 1 (Empleado)"))
cola_impresion.put((1, "Documento 2 (Empleado)"))
cola_impresion.put((1, "Documento 3 (Empleado)"))

#b. Imprimir el primer documento de la cola
primer_documento = cola_impresion.get()[1]
print("Imprimir:", primer_documento)

#c. Cargar dos documentos del staff de TI
cola_impresion.put((2, "Documento 4 (Staff TI)"))
cola_impresion.put((2, "Documento 5 (Staff TI)"))

#d. Cargar un documento del gerente
cola_impresion.put((3, "Documento 6 (Gerente)"))

#e. Imprimir los dos primeros documentos de la cola
primer_documento = cola_impresion.get()[1]
segundo_documento = cola_impresion.get()[1]
print("Imprimir:", primer_documento)
print("Imprimir:", segundo_documento)

#f. Cargar dos documentos de empleados y uno de gerente
cola_impresion.put((1, "Documento 7 (Empleado)"))
cola_impresion.put((1, "Documento 8 (Empleado)"))
cola_impresion.put((3, "Documento 9 (Gerente)"))

#g. Imprimir todos los documentos de la cola de impresión
while not cola_impresion.empty():
    documento = cola_impresion.get()[1]
    print("Imprimir:", documento)
