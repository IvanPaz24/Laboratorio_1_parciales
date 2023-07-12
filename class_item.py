import pygame
'''
Inicializa una instancia de la clase Item con la imagen proporcionada, 
la posición inicial y el tamaño del ítem. La imagen se escala al tamaño especificado y se crea un rectángulo que la rodea.
No se definen otros métodos en esta clase.
'''
class Item():
    def __init__(self, imagen,posicion_inicial, tamaño):
        self.imagen = imagen
        self.imagen = pygame.transform.scale(self.imagen,tamaño)
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = posicion_inicial[0] 
        self.rectangulo.y = posicion_inicial[1]
        self.flag_item = True