#en este documento establecemos una de las clases para la herencia múltiple

class figuraGeometrica:
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto
    
    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self,ancho):
        self._ancho = ancho
    
    @property
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self, alto):
        self._alto = alto
    
    def __str__(self): #Revisar que el código está bien
        return f'Ancho: {self.ancho}, Alto: {self.alto}'