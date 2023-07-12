from configuraciones import *
import pygame
from class_plataforma import Plataforma
# from class_patrulla import Patraulla
# from class_jefe import Jefe
import time

pygame.mixer.init()
'''
Inicializa un objeto Personaje. Recibe varios parámetros que definen las características del personaje, 
como el tamaño, las animaciones, la posicion_inicial, la velocidad, la dirección donde_mira y el tamaño_pantalla. 
Establece los atributos correspondientes del objeto Personaje utilizando los valores proporcionados.
'''
class Personaje:
    def __init__(self, tamaño, animaciones,posicion_inicial, velocidad, donde_mira, tamaño_pantalla):
        #confeccion
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.largo_pantalla = tamaño_pantalla[0]
        self.alto_pantalla = tamaño_pantalla[1]
        #Gravedad
        self.gravedad = 1
        self.poctencia_salto = -25
        self.limite_velocidad_caida = 20
        self.esta_saltando = False
        self.esta_chocando = False
        #ANIMACIONES
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.animaciones = animaciones
        self.reescalar_animaciones()
        self.donde_mira = donde_mira
        #rectangulos
        self.rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        self.posicion_inicial_x = posicion_inicial[0]
        self.rectangulo.x = posicion_inicial[0]
        self.posicion_inicial_y = posicion_inicial[1]
        self.rectangulo.y = posicion_inicial[1]
        self.width = self.animaciones["camina_derecha"][0].get_width()
        self.height = self.animaciones["camina_derecha"][0].get_height()
        self.lados = obtener_rectangulos(self.rectangulo)
        #movimiento
        self.velocidad = velocidad
        self.desplazamiento_y = 0
        #vida
        self.vida = 3
        self.score = 0
        self.sonido_disparo = pygame.mixer.Sound("Mis recursos/sonidos/sonido_disparo.wav")
        self.sonido_disparo.set_volume(0.2)

    '''
    Reescala las imágenes de las animaciones del personaje al tamaño especificado.
    '''
    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], (self.ancho, self.alto))
    '''
    Reproduce una animación del personaje en la pantalla. Recibe el nombre de la animación (que_animacion) y 
    la muestra en la posición actual del personaje.
    '''
    def animar(self,pantalla,que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
    
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1
    '''
    Mueve el personaje horizontalmente con una velocidad determinada.
    '''
    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad
    '''
    Actualiza el estado del personaje, gestionando sus movimientos, animaciones, 
    gravedad y colisiones con las plataformas.
    '''
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
        self.platafoma_colision(lista_plataforma)
    '''
    Aplica la gravedad al personaje, haciendo que caiga si no está sobre una plataforma.
    '''
    def aplicar_gravedad(self, pantalla, lista_plataforma:Plataforma):
        if self.esta_saltando:
            if self.donde_mira == False:
                self.animar(pantalla,"salta")
            else :
                self.animar(pantalla,"salta_izquierda")   
            
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad

        for piso in lista_plataforma:
            if self.lados["bottom"].colliderect(piso.lados["top"]):
                self.esta_saltando = False
                self.desplazamiento_y = 0
                self.lados["main"].bottom = piso.lados["main"].top + 5
                break
            else:
                self.esta_saltando = True
    '''
    Verifica si el personaje ha sido alcanzado por un proyectil y devuelve un valor booleano que indica si está muerto.
    '''
    def muerto(self, proyectil):
        flag = False
        if self.rectangulo.colliderect(proyectil.rectangulo):
            flag = True

        return flag
    '''
    Verifica si el personaje ha golpeado a un enemigo y realiza las acciones correspondientes.
    '''
    def golpea(self,lista_enemigo):
        for enemigo in lista_enemigo:
            if self.rectangulo.colliderect(enemigo.rectangulo):
                enemigo.desaparecer_personaje(lista_enemigo)
                for lado in self.lados:
                    # self.lados[lado].x += self.velocidad
                    self.lados[lado].y += self.desplazamiento_y

        self.desplazamiento_y = 0
    '''
    Verifica si el personaje ha sido alcanzado por una bala y realiza las acciones correspondientes.
    '''
    def bala_colision(self, largo, lista_balas, lista_plataformas):
        for bala_enemigo in lista_balas:
            if self.muerto(bala_enemigo):
                lista_balas.pop(lista_balas.index(bala_enemigo))
                self.score -= 100
                self.vida -= 1

            if bala_enemigo.rectangulo.x < largo and bala_enemigo.rectangulo.x > 0:
                bala_enemigo.rectangulo.x += bala_enemigo.velocidad
            else:
                lista_balas.pop(lista_balas.index(bala_enemigo))

            for plataforma in lista_plataformas:
                if bala_enemigo.rectangulo.colliderect(plataforma.lados["main"]):
                    lista_balas.pop(lista_balas.index(bala_enemigo))
    '''
    Verifica si el personaje colisiona con una plataforma y ajusta su posición y velocidad en consecuencia.
    '''
    def platafoma_colision(self, lista_plataformas):
        for plataforma in lista_plataformas:
            if self.lados["left"].colliderect(plataforma.lados["right"]):
                for lado in self.lados:
                    self.lados[lado].x += self.velocidad
                    self.lados[lado].y += self.desplazamiento_y
                self.esta_chocando = True
            elif self.lados["right"].colliderect(plataforma.lados["left"]):
                for lado in self.lados:
                    self.lados[lado].x -= self.velocidad
                    self.lados[lado].y += self.desplazamiento_y
                self.esta_chocando = True
            else:
                self.esta_chocando = False
                
            if self.esta_chocando:
                self.desplazamiento_y = 0
    '''
    Verifica si el personaje colisiona con un enemigo y realiza las acciones correspondientes.
    '''
    def colision_enemigo(self,enemigo):
        if self.lados["main"].colliderect(enemigo.lados["main"]):
            self.vida -= 1
            self.score -= 100
            for lado in self.lados:
                self.lados[lado].x = self.posicion_inicial_x
                self.lados = obtener_rectangulos(self.rectangulo)