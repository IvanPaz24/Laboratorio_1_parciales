from class_personaje import Personaje
from configuraciones import *
import pygame, sys
import random

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

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], (self.largo, self.ancho))

    def animar(self, pantalla, que_animacion: str):
        return super().animar(pantalla, que_animacion)
    
    def muerto(self, proyectil,lista_enemigo):
        flag = False
        if proyectil.rectangulo.colliderect(self.rectangulo):
            self.desaparecer_personaje(lista_enemigo)
            flag = True

        return flag
        # return super().muerto(proyectil,largo,pantalla)
            
    def desaparecer_personaje(self, lista_enemigo:list):
        # for enemigo in lista_enemigo:
        lista_enemigo.remove(self)
        # if largo / 2 < largo:
        #     self.animar(pantalla, "quieto_enemigo_izquirda")

    def bala_colision(self, largo,lista_balas, lista_enemigos, personaje):
        for bala in lista_balas:
            if self.muerto(bala, lista_enemigos):
                lista_balas.pop(lista_balas.index(bala))
                personaje.score += 100

            if bala.rectangulo.x < largo and bala.rectangulo.x > 0:
                bala.rectangulo.x += bala.velocidad
            else:
                lista_balas.pop(lista_balas.index(bala)) 

    def donde_apunta(self, largo):
        if self.rectangulo.x > largo/2:
            self.direccion_enemigo = -1
        elif self.rectangulo.x < largo:
            self.direccion_enemigo = 1 
        return self.direccion_enemigo 
