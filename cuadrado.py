#en este documento establecemos la clase hija que va a heredar de 2 clases

from figuraGeometrica import figuraGeometrica
from color import Color

class Cuadrado(figuraGeometrica,Color): #deven añadirse en el orden en el que se importan
    def __init__(self,lado, color):
        figuraGeometrica.__init__(self, lado, lado) #se establece que 'lado' será igual al lado y al ancho (ya que como es un cuadrado ambos son iguales)
        Color.__init__(self, color) #como hay 2 clases padres, no se puede usar 'super()', ya que podría dar lugar a problemas, en su lugar, usamos el nombre de la propia clase (cada una de las clases) y importamos 'self' (debido a que estamos usando directamente a la clase)
        self.lado = lado #este código solo es necesario debido a la línea 20, donde se quiere imprimir la propiedad 'self.lado'
    
    def calcularArea(self):
        return self.alto * self.ancho # se usan las propiedades de la clase padre (se podría usar la variable de 'lado'. Pero no es necesario ya que podemos trabajar directamente sobre las variables de la clase padre). La variable de 'lado' se crea unicamente para importar correctamente las propiedades de la clase padre

#Cuando vayamos a crear un nuevo 'cuadrado', lo haríamos de la siguiente forma:

cuadrado1 = Cuadrado(5, 'rojo') # añadimos solo un valor de medida porque ya hemos añadido en la declaración de la clase que solo recoja 2 valores, de color y de lado. La variable de lado apunta al alto y ancho, por lo que también podemos acceder al alto y ancho:
print(cuadrado1.alto)
print(cuadrado1.ancho)
print(cuadrado1.lado) #está relacionado a 'alto' y 'ancho' (LEER LINEA 10)
print(cuadrado1.calcularArea())
