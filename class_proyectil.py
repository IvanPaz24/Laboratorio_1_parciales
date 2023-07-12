import pygame
from configuraciones import *
'''
El constructor de la clase Proyectil que inicializa un objeto Proyectil. 
Recibe cinco parámetros: tamaño (el tamaño del proyectil), x (la coordenada x inicial del proyectil), 
y (la coordenada y inicial del proyectil), velocidad (la velocidad del proyectil) 
y direccion (la dirección del proyectil, que indica si se mueve hacia la izquierda o hacia la derecha). 
El constructor establece los atributos direccion, proyectil, rectangulo, rectangulo.x, rectangulo.y y 
velocidad del objeto Proyectil.
'''
class Proyectil:
    def __init__(self ,tamaño, x, y, velocidad, direccion):
        self.direccion = direccion
        self.proyectil = pygame.transform.scale(proyectil, tamaño)
        self.rectangulo = self.proyectil.get_rect()
        self.rectangulo.x = x
        self.rectangulo.y = y 
        self.velocidad = velocidad * self.direccion

    '''
    Método que muestra el proyectil en la pantalla. 
    Utiliza el método blit() para dibujar el proyectil en la posición actual definida por 
    el atributo rectangulo sobre la pantalla especificada.
    '''
    def animar(self, pantalla):
        pantalla.blit(self.proyectil, self.rectangulo)
        