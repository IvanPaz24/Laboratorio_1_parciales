import pygame
from configuraciones import *

class Plataforma:
    def __init__(self,x,y,ancho,alto):
        # self.ancho = tamaño[0]
        # self.alto = tamaño[1]
        # self.x = posicion[0]
        # self.y = posicion[1]
        self.ancho = ancho
        self.alto = alto
        self.x = x
        self.y = y
        self.rectangulo = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        
    def crear_lados(self):
        self.lados = obtener_rectangulos(self.rectangulo)


