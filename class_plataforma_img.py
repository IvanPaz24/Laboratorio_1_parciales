import pygame
from class_plataforma import Plataforma
from configuraciones import *
'''
El constructor de la clase Plataforma_Img que inicializa un objeto Plataforma_Img. 
Recibe cinco parámetros: path (la ruta de la imagen de la plataforma), x (la coordenada x de la plataforma),
y (la coordenada y de la plataforma), alto (la altura de la plataforma) y ancho (el ancho de la plataforma). 
Carga la imagen de la plataforma utilizando pygame.image.load(), redimensiona la imagen con pygame.transform.scale() 
y establece el atributo imagen y el atributo rectangulo del objeto Plataforma_Img.
'''
class Plataforma_Img(Plataforma):
    def __init__(self, path, x , y, alto, ancho):
            self.imagen = pygame.image.load(path)
            self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
    
            self.rectangulo = self.imagen.get_rect()
            self.rectangulo.x = x
            self.rectangulo.y = y
    '''
    Método que crea los lados de la plataforma. 
    Llama al método crear_lados() de la clase base Plataforma usando super().crear_lados().
    '''
    def crear_lados(self):
        return super().crear_lados()
    '''
    Método que muestra la plataforma en la pantalla. 
    Utiliza el método blit() para dibujar la imagen de la plataforma en la posición actual definida 
    por el atributo rectangulo sobre la pantalla especificada.
    '''
    def mostrar(self, pantalla):
        pantalla.blit(self.imagen, self.rectangulo)