class Pila():
    """Stack class"""

    def __init__(self):
        self.__elements = []

    def push(self, dato):
        self.__elements.append(dato)

    def pop(self):
        if self.size() > 0:
            dato = self.__elements.pop()
            return dato

    def size(self):
        return len(self.__elements)

    def on_top(self):
        if self.size() > 0:
            return self.__elements[-1]