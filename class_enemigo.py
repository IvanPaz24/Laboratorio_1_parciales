from configuraciones import *
import pygame, sys
import random
from class_personaje import Personaje

'''
Inicializa un objeto Enemigo. Recibe la posición inicial (posicion), el tamaño (tamaño) y 
un diccionario de animaciones (animaciones). Establece el largo y ancho del enemigo, 
inicializa el contador de pasos, guarda las animaciones y las reescala al tamaño especificado. 
Crea un rectángulo para el enemigo y establece su posición. Obtiene los lados del rectángulo. 
Configura la dirección del enemigo y carga el sonido de disparo.
'''
class Enemigo(Personaje):
    def __init__(self,posicion, tamaño, animaciones):
        self.largo = tamaño[0]
        self.ancho = tamaño[1]
        self.contador_pasos = 0
        self.animaciones = animaciones
        self.reescalar_animaciones()
        self.rectangulo = self.animaciones["quieto_enemigo"][0].get_rect()
        self.rectangulo.x = posicion[0]
        self.rectangulo.y = posicion[1]
        self.lados = obtener_rectangulos(self.rectangulo)
        self.direccion_enemigo = 0
        self.sonido_disparo = pygame.mixer.Sound("Mis recursos/sonidos/sonido_disparo.wav")
        self.sonido_disparo.set_volume(0.2)
    '''
    Reescala todas las animaciones del enemigo al tamaño especificado.
    '''
    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], (self.largo, self.ancho))
    '''
    Muestra la animación correspondiente del enemigo en la pantalla.
    '''
    def animar(self, pantalla, que_animacion: str):
        return super().animar(pantalla, que_animacion)
    '''
    Comprueba si el enemigo ha sido golpeado por un proyectil. Si es así, elimina al enemigo de la lista de enemigos.
    '''
    def muerto(self, proyectil,lista_enemigo):
        flag = False
        if proyectil.rectangulo.colliderect(self.rectangulo):
            self.desaparecer_personaje(lista_enemigo)
            flag = True

        return flag
    '''
    Elimina al enemigo de la lista de enemigos.
    '''
    def desaparecer_personaje(self, lista_enemigo:list):
        lista_enemigo.remove(self)
    '''
    Verifica si las balas colisionan con el enemigo. Si colisionan, elimina la bala y aumenta la puntuación del personaje.
    '''
    def bala_colision(self, largo,lista_balas, lista_enemigos, personaje, lista_plataforma):
        for bala in lista_balas:
            if self.muerto(bala, lista_enemigos):
                lista_balas.pop(lista_balas.index(bala))
                personaje.score += 100

            if bala.rectangulo.x < largo and bala.rectangulo.x > 0:
                bala.rectangulo.x += bala.velocidad
            else:
                lista_balas.pop(lista_balas.index(bala)) 
            
            for plataforma in lista_plataforma:
                if bala.rectangulo.colliderect(plataforma.lados["main"]):
                    lista_balas.pop(lista_balas.index(bala))
    '''
    Determina la dirección en la que el enemigo apunta en función de su posición en relación al ancho de la pantalla.
    '''
    def donde_apunta(self, largo):
        if self.rectangulo.x > largo/2:
            self.direccion_enemigo = -1
        elif self.rectangulo.x < largo:
            self.direccion_enemigo = 1 
        return self.direccion_enemigo 
    