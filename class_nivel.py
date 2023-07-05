import pygame
from class_enemigo import Enemigo
from configuraciones import *
import pygame, sys
from pygame.locals import *
from class_personaje import Personaje
from class_plataforma import Plataforma
from class_plataforma_img import Plataforma_Img
from class_proyectil import Proyectil
from class_enemigo import Enemigo
from class_item import Item
from cabiar_modo import *
DEBUG = False  
class Nivel():
    def __init__(self, pantalla, personaje_pricipal, lista_plataformas, imagen_fondo, lista_enemigos, largo_pantalla, 
                balas_personaje, balas_enemigo, flag_item, item, fuente, contador_nivel):
        self.slave = pantalla
        self.jugador = personaje_pricipal
        self.plataformas = lista_plataformas
        self.imagen_fondo = imagen_fondo
        self.enemigos = lista_enemigos
        self.largo_pantalla = largo_pantalla
        self.balas_personaje = balas_personaje
        self.balas_enemigo = balas_enemigo
        self.item = item
        self.lista_item = [item]
        self.flag_item = flag_item
        self.fuente = fuente
        self.cronometro = contador_nivel
        self.turno_proyectiles = 0
        self.contador_balas_enemigo = 0

    def update(self, lista_eventos):
        # turno_proyectiles = 0
        # contador_balas_enemigo = 0

        # for evento in lista_eventos:
            # if evento.type == pygame.QUIT:
            #     pygame.quit()
            #     sys.exit()
            # if evento.type == pygame.KEYDOWN:
            #     if evento.key == pygame.K_TAB:
            #         cambiar_modo()
            #         self.dibujar_rectangulos()
        
        self.slave.blit(self.slave, (0,0))

        if self.turno_proyectiles > 0:
            self.turno_proyectiles += 1
        if self.turno_proyectiles > 3:
            self.turno_proyectiles = 0

        for enemigo in self.enemigos:
            enemigo.bala_colision(self.largo_pantalla,self.balas_personaje, self.enemigos, self.jugador)

        self.jugador.bala_colision(self.largo_pantalla,self.balas_enemigo)

        self.contador_balas_enemigo += 1
    
        if self.contador_balas_enemigo == 100:
            for enemigo in self.enemigos:
                direccion_enemigo = enemigo.donde_apunta(self.largo_pantalla)

                if len(self.balas_personaje) < 1:
                    self.balas_enemigo.append(Proyectil((20,20), enemigo.rectangulo.centerx, enemigo.rectangulo.centery, 45, direccion_enemigo))
                    self.turno_proyectiles = 1
                    self.contador_balas_enemigo = 0
        
        for item in self.lista_item:
            if self.jugador.lados["main"].colliderect(item.rectangulo):
                self.jugador.score += 500
                self.lista_item.pop(self.lista_item.index(item))
                self.jugador.vida += 1
                self.flag_item = False

        self.leer_teclas()
        self.actualizar_pantalla()

    def actualizar_pantalla(self):
        self.slave.blit(self.imagen_fondo, (0,0))
        self.jugador.update(self.slave, self.plataformas)
        for plataforma in self.plataformas:
            if type(plataforma) is Plataforma_Img:
                plataforma.mostrar(self.slave)
        for enemigo in self.enemigos:
            if enemigo.rectangulo.x > self.largo_pantalla/2:
                enemigo.animar(self.slave, "quieto_enemigo")
            else:
                enemigo.animar(self.slave, "quieto_enemigo_derecha")
        # enemigo.animar(self.slave, "quieto_enemigo_derecha")
        
        # enemigo.update(self.slave, lista_plataforma)
        for bala in self.balas_personaje:
            bala.animar(self.slave)
            # enemigo.muerto(bala)
        
        for bala in self.balas_enemigo:
            bala.animar(self.slave)

        if self.flag_item:
            self.slave.blit(self.item.imagen, self.item.rectangulo)
        score = self.fuente.render(f"Score {self.jugador.score}",False, "Green", "Blue")
        vida_actual = self.fuente.render(f"Vidas:{self.jugador.vida}",False, "Red")

        self.slave.blit(score, (0,0))
        self.slave.blit(vida_actual, (1700, 0))

        # minutos = self.cronometro // 60
        # segundos = self.cronometro % 60
        self.cronometro -= 1
        if self.cronometro > 0:
            minutos = self.cronometro // 60
            segundos = self.cronometro % 60
        else:
            minutos = 0
            segundos = 0
        tiempo_actual = self.fuente.render(f"Tiempo:{minutos}:{segundos}", False, "Black")
        self.slave.blit(tiempo_actual,(700,0))
        


    def leer_teclas(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.jugador.que_hace = "derecha"
            self.jugador.donde_mira = False
        elif keys[pygame.K_LEFT]:
            self.jugador.que_hace = "izquierda"
            self.jugador.donde_mira = True
        elif keys[pygame.K_UP]:
            if self.jugador.donde_mira == False:
                self.jugador.que_hace = "salta"
            else:
                self.jugador.que_hace = "salta_izquierda"
        elif keys[pygame.K_f]:
            if self.jugador.donde_mira == False:
                self.jugador.que_hace = "golpe"
                self.jugador.golpea(self.enemigos)
            else:
                self.jugador.que_hace = "golpe_izquierda"
                self.jugador.golpea(self.enemigos)
        elif mouse[0] and self.turno_proyectiles == 0:
            if self.jugador.donde_mira == False:
                direccion = 1
            elif self.jugador.donde_mira == True:
                direccion = -1
            else:
                direccion = 0

            if len(self.balas_personaje) < 4:
                self.balas_personaje.append(Proyectil((20,20),self.jugador.rectangulo.centerx, self.jugador.rectangulo.centery, 50, direccion))
                self.turno_proyectiles = 1

        else:
            if self.jugador.donde_mira == False:
                self.jugador.que_hace = "quieto"
            else:
                self.jugador.que_hace = "quieto_izquierda"

    # def dibujar_rectangulos(self):
    #     if get_mode():
    #         for plataforma in self.plataformas:
    #             for lado in plataforma.lados:
    #                 pygame.draw.rect(self.slave,"Blue",plataforma.lados[lado] ,2)