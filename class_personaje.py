from configuraciones import *
import pygame
from class_plataforma import *

class Personaje:
    def __init__(self, tamaño, animaciones,posicion_inicial, velocidad, donde_mira, tamaño_pantalla):
        #confeccion
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.largo_pantalla = tamaño_pantalla[0]
        self.alto_pantalla = tamaño_pantalla[1]
        #Gravedad
        self.gravedad = 1
        self.poctencia_salto = -20
        self.limite_velocidad_caida = 15
        self.esta_saltando = False
        #ANIMACIONES
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.animaciones = animaciones
        self.reescalar_animaciones()
        self.donde_mira = donde_mira
        #rectangulos
        self.rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(self.rectangulo)
        #movimiento
        self.velocidad = velocidad
        self.desplazamiento_y = 0
    #quieto - salta - camina_derecha - camina_izquierda
    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], (self.ancho, self.alto))

    def animar(self,pantalla,que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
    
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1

    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad


    def update(self, pantalla, lista_plataforma):
        match self.que_hace:
            case "derecha":
                if not self.esta_saltando:
                    #animar_personaje
                    self.animar(pantalla, "camina_derecha")
                nueva_x = self.rectangulo.x + 10
                if nueva_x < self.largo_pantalla - self.ancho:
                    self.mover(self.velocidad)
            case "izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_izquierda")
                nueva_x = self.rectangulo.x - 10
                if nueva_x > 0:
                    self.mover(self.velocidad*-1)
            case "salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.poctencia_salto 
            case "salta_izquierda":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.poctencia_salto 
            case "quieto":
                if not self.esta_saltando:
                #animar
                    self.animar(pantalla, "quieto")
            case "quieto_izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla, "quieto_izquierda")
            case "golpe":
                if not self.esta_saltando:
                    self.animar(pantalla ,"golpe")
            case "golpe_izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla ,"golpe_izquierda")

        self.aplicar_gravedad(pantalla, lista_plataforma)

    def aplicar_gravedad(self, pantalla, lista_plataforma:Plataforma):
        if self.esta_saltando:
            if self.donde_mira == False:
                self.animar(pantalla,"salta")
            else:
                self.animar(pantalla,"salta_izquierda")
        
            
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad

        for piso in lista_plataforma:
            if self.lados["bottom"].colliderect(piso["top"]):
                self.esta_saltando = False
                self.desplazamiento_y = 0
                self.lados["main"].bottom = piso["main"].top + 5
                break
            else:
                self.esta_saltando = True
    
    def muerto(self, proyectil, largo, pantalla):
        flag = False
        if proyectil.rectangulo.colliderect(self.rectangulo):
            self.desaparecer_personaje()
            flag = True

        return flag
    
    def golpea(self,lista_enemigo):
        for enemigo in lista_enemigo:
            if self.rectangulo.colliderect(enemigo.rectangulo):
                enemigo.desaparecer_personaje(lista_enemigo)
            
    def desaparecer_personaje(self):
        for lado in self.lados:
            self.lados[lado].x = 0