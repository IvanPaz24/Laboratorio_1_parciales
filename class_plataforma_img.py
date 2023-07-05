import pygame
from class_plataforma import Plataforma
from configuraciones import *

class Plataforma_Img(Plataforma):
    def __init__(self, path, x , y, alto, ancho):
            self.imagen = pygame.image.load(path)
            self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
    
            self.rectangulo = self.imagen.get_rect()
            self.rectangulo.x = x
            self.rectangulo.y = y

    def crear_lados(self):
        return super().crear_lados()
    
    def mostrar(self, pantalla):
        pantalla.blit(self.imagen, self.rectangulo)