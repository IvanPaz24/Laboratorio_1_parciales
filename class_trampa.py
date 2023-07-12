import pygame
from configuraciones import *

'''
El constructor de la clase Trampa que inicializa un objeto Trampa. 
Recibe tres parámetros: tamaño (el tamaño de la trampa), x (la coordenada x inicial de la trampa) e 
y (la coordenada y inicial de la trampa). El constructor establece los atributos trampa, rectangulo, 
rectangulo.x y rectangulo.y del objeto Trampa.
'''
class Trampa:
    def __init__(self ,tamaño, x, y):
        self.trampa = pygame.transform.scale(trampa_imagen, tamaño)
        self.rectangulo = self.trampa.get_rect()
        self.rectangulo.x = x
        self.rectangulo.y = y

    '''
    Método que muestra la trampa en la pantalla. 
    Utiliza el método blit() para dibujar la trampa en la posición actual definida por 
    el atributo rectangulo sobre la pantalla especificada.
    '''
    def animar(self, pantalla):
        pantalla.blit(self.trampa, self.rectangulo)
    '''
    Método que verifica si hay colisión entre la trampa y el personaje. 
    Si hay colisión, reduce la vida del personaje en 1 y resta 100 puntos a su puntuación. 
    Luego, ajusta las posiciones de los lados del personaje a su posición inicial mediante 
    la asignación de personaje.lados[lado].x = personaje.posicion_inicial_x.
    '''
    def colision_personaje(self, personaje):
        if self.rectangulo.colliderect(personaje.lados["main"]):
            personaje.vida -= 1
            personaje.score -= 100
            for lado in personaje.lados:
                personaje.lados[lado].x = personaje.posicion_inicial_x
                personaje.lados = obtener_rectangulos(personaje.rectangulo)
