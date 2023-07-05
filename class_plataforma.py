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

    # def colision_pared(self,personaje):
    #     if personaje.rectangulo.colliderect(self.rectangulo):
    #         if personaje.velocidad > 0:  # El personaje se mueve hacia la derecha
    #             personaje.rectangulo.right = self.rectangulo.left  # Ajustar la posición a la izquierda de la plataforma
    #         elif personaje.velocidad < 0:  # El personaje se mueve hacia la izquierda
    #             personaje.rectangulo.left = self.rectangulo.right  # Ajustar la posición a la derecha de la plataforma
    #         personaje.velocidad = 0 


