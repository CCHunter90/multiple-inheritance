from figuraGeometrica import figuraGeometrica
from color import Color

class Rectangulo(figuraGeometrica,Color):
    def __init__(self,color,ancho, alto): #IMPORTANTE EL ORDEN A LA HORA DE ESTABLECER LUEGO LOS ELEMENTOS
        figuraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self,color)
    def calcularArea(self):
        return self.ancho * self.alto
    def __str__(self):
        return f'{figuraGeometrica.__str__(self)}, Color: {self.color}'

#Prueba creación del objeto

rectangulo1 = Rectangulo('marron',20,10)

print(rectangulo1)
print('Calcular Área'.center(20,'-'))
print(rectangulo1.calcularArea())