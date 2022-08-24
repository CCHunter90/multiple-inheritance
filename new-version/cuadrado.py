from color import Color
from figuraGeometrica import figuraGeometrica

class Cuadrado(Color,figuraGeometrica):
    def __init__(self, color, lado):
        Color.__init__(self, color)
        figuraGeometrica.__init__(self, lado, lado)
    
    def calcularArea(self):
        return self.ancho * self.alto

    def __str__(self):
        return f'{figuraGeometrica.__str__(self)}, Color: {self.color}'

#Pruebas de la clase (objeto de prueba)
cuadrado1 = Cuadrado('verde', 10)

print(cuadrado1)
print(cuadrado1.calcularArea())
