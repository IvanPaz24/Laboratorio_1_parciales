import pygame
from configuraciones import *
'''
Inicializa una instancia de la clase Plataforma con los valores especificados para el ancho, alto, coordenadas x e y.
'''
class Plataforma:
    def __init__(self,x,y,ancho,alto):
        self.ancho = ancho
        self.alto = alto
        self.x = x
        self.y = y
        self.rectangulo = pygame.Rect(self.x, self.y, self.ancho, self.alto)
    '''
    crear_lados(): Crea los lados de la plataforma utilizando la función auxiliar obtener_rectangulos(). 
    Los lados de la plataforma se almacenan en el atributo lados.
    '''
    def crear_lados(self):
        self.lados = obtener_rectangulos(self.rectangulo)


