import pygame
from configuraciones import *

class Proyectil:
    def __init__(self ,tamaño, x, y, velocidad, direccion):
        self.direccion = direccion
        self.proyectil = pygame.transform.scale(proyectil, tamaño)
        self.rectangulo = self.proyectil.get_rect()
        self.rectangulo.x = x
        self.rectangulo.y = y 
        self.velocidad = velocidad * self.direccion

    def animar(self, pantalla):
        # self.rectangulo = self.proyectil.get_rect()
        pantalla.blit(self.proyectil, self.rectangulo)
        