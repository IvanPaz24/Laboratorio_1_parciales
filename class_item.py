import pygame

class Item():
    def __init__(self, imagen,posicion_inicial, tamaño):
        self.imagen = imagen
        self.imagen = pygame.transform.scale(self.imagen,tamaño)
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = posicion_inicial[0] 
        self.rectangulo.y = posicion_inicial[1]