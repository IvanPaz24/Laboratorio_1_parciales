import pygame
from cabiar_modo import *
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
from class_patrulla import Patraulla
from class_jefe import Jefe
DEBUG = False  
def cambiar_modo():     
    global DEBUG     
    DEBUG = not DEBUG  

def get_mode():     
    return DEBUG
'''
Inicializa un objeto Nivel. Recibe múltiples parámetros que definen las características del nivel. 
Establece los atributos correspondientes del objeto Nivel utilizando los valores proporcionados.
'''
class Nivel():
    def __init__(self, pantalla, personaje_pricipal, lista_plataformas, imagen_fondo, lista_enemigos, largo_pantalla, 
                balas_personaje, balas_enemigo, item, fuente, contador_nivel, trampa, nombre_jugador):
        self.slave = pantalla
        self.jugador = personaje_pricipal
        self.plataformas = lista_plataformas
        self.imagen_fondo = imagen_fondo
        self.enemigos = lista_enemigos
        self.largo_pantalla = largo_pantalla
        self.balas_personaje = balas_personaje
        self.balas_enemigo = balas_enemigo
        # self.item = item
        self.lista_item = item
        self.fuente = fuente
        self.cronometro = contador_nivel
        self.turno_proyectiles = 0
        self.contador_balas_enemigo = 0
        self.contador_enemigo = 10
        self.trampa = trampa
        self.largo = pantalla.get_width()
        self.ancho = pantalla.get_height()
        self.score = 0
        self.nombre_usuario = nombre_jugador
        self.datos_guardados = False
        self.segundos = 60

    '''
    Actualiza el estado del nivel, gestionando colisiones, movimientos, acciones de personajes y 
    enemigos, tiempo, puntuación y actualización de la pantalla.
    '''
    def update(self, lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                # if evento.key == pygame.K_TAB:
                #     cambiar_modo()
                self.dibujar_plataformas(evento)
        self.slave.blit(self.slave, (0,0))

        if self.turno_proyectiles > 0:
            self.turno_proyectiles += 1
        if self.turno_proyectiles > 3:
            self.turno_proyectiles = 0

        for enemigo in self.enemigos:
            if type(enemigo) == Enemigo:
                enemigo.bala_colision(self.largo_pantalla,self.balas_personaje,self.enemigos, self.jugador, 
                self.plataformas)
            if type(enemigo) == Jefe:
                enemigo.bala_colision(self.largo_pantalla,self.balas_personaje,self.enemigos,self.jugador
                , self.plataformas)
                self.jugador.colision_enemigo(enemigo)
            if type(enemigo) == Patraulla:
                enemigo.bala_colision(self.largo_pantalla,self.balas_personaje,self.jugador
                ,self.plataformas)
                self.jugador.colision_enemigo(enemigo)

        self.jugador.bala_colision(self.largo_pantalla,self.balas_enemigo, self.plataformas)

        self.contador_balas_enemigo += 1
    
        if self.contador_balas_enemigo == 70:
            for enemigo in self.enemigos:
                direccion_enemigo = enemigo.donde_apunta(self.largo_pantalla)
                if type(enemigo) == Enemigo:
                    if len(self.balas_personaje) < 1:
                        self.balas_enemigo.append(Proyectil((20,20), 
                        enemigo.rectangulo.centerx, enemigo.rectangulo.centery - 45, 45, direccion_enemigo))
                        self.turno_proyectiles = 1
                        self.contador_balas_enemigo = 0
                        enemigo.sonido_disparo.play()
                
                if type(enemigo) == Patraulla or type(enemigo) == Jefe:
                    if len(self.balas_personaje) < 1:
                        self.balas_enemigo.append(Proyectil((20,20), enemigo.rectangulo.centerx, 
                        enemigo.rectangulo.centery - 45, 45, enemigo.direccion))
                        self.turno_proyectiles = 1
                        self.contador_balas_enemigo = 0
                        enemigo.sonido_disparo.play()

        
        for item in self.lista_item:
            if self.jugador.lados["main"].colliderect(item.rectangulo):
                self.jugador.score += 500
                self.lista_item.pop(self.lista_item.index(item))
                self.jugador.vida += 1
                item.flag_item = False
        
        self.trampa.colision_personaje(self.jugador)
        
        self.leer_teclas()
        self.actualizar_pantalla()
    '''
    Actualiza el contenido de la pantalla, dibujando los elementos del nivel.
    '''
    def actualizar_pantalla(self):
        self.slave.blit(self.imagen_fondo, (0,0))
        self.jugador.update(self.slave, self.plataformas)
        for plataforma in self.plataformas:
            if type(plataforma) is Plataforma_Img:
                plataforma.mostrar(self.slave)
        for enemigo in self.enemigos:
            if enemigo.rectangulo.x > self.largo_pantalla/2 and type(enemigo) is Enemigo:
                enemigo.animar(self.slave, "quieto_enemigo")
            elif type(enemigo) == Enemigo:
                enemigo.animar(self.slave, "quieto_enemigo_derecha")

            if type(enemigo) == Patraulla:
                enemigo.se_mueve(self.slave, self.plataformas)
            
            if type(enemigo) == Jefe:
                enemigo.se_mueve(self.slave, self.plataformas, self.fuente)
        
        for bala in self.balas_personaje:
            bala.animar(self.slave)
        
        for bala in self.balas_enemigo:
            bala.animar(self.slave)

        for item in self.lista_item:
            if item.flag_item:
                self.slave.blit(item.imagen, item.rectangulo)

        score = self.fuente.render(f"Score {self.jugador.score}",False,"Blue")
        vida_actual = self.fuente.render(f"Vidas:{self.jugador.vida}",False, "Red")

        self.slave.blit(score, (0,0))
        self.slave.blit(vida_actual, (1700, 0))

        self.segundos -= 1
        if self.cronometro > 0:
            if self.segundos == 0:
                self.cronometro -= 1
                self.segundos = 60
        else:
            self.cronometro = 0
            self.segundos = 0
        tiempo_actual = self.fuente.render(f"Tiempo:{self.cronometro}:{self.segundos}", False, "Black")
        self.slave.blit(tiempo_actual,(700,0))
        self.trampa.animar(self.slave)

        game_over = pygame.image.load("Mis recursos/game_over.png")
        game_over = pygame.transform.scale(game_over, (self.largo,self.ancho))
        if self.jugador.vida < 1 or self.cronometro == 0:
            self.guardar("datos_score.json")
            self.slave.blit(game_over,(0,0))
        
        mision_complete = pygame.image.load("Mis recursos/mision_complete.jpeg")
        mision_complete = pygame.transform.scale(mision_complete, (self.largo,self.ancho))
        if len(self.enemigos) < 1:
            self.guardar("datos_score.json")
            self.slave.blit(mision_complete,(0,0))
    '''
    Lee las teclas presionadas y el estado del mouse para determinar las acciones del personaje.
    '''
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
            self.jugador.sonido_disparo.play()
            if self.jugador.donde_mira == False:
                direccion = 1
            elif self.jugador.donde_mira == True:
                direccion = -1
            else:
                direccion = 0

            if len(self.balas_personaje) < 4:
                self.balas_personaje.append(Proyectil((20,20),self.jugador.rectangulo.centerx, 
                self.jugador.rectangulo.centery, 50, direccion))
                self.turno_proyectiles = 1

        else:
            if self.jugador.donde_mira == False:
                self.jugador.que_hace = "quieto"
            else:
                self.jugador.que_hace = "quieto_izquierda"
    '''
    Guarda los datos de puntuación en un archivo JSON.
    '''
    def guardar(self, path):
        if self.datos_guardados == False:
            dicccionario_score = {}
            dicccionario_score = leer_json(path)
            if self.nombre_usuario in dicccionario_score:
                dicccionario_score[self.nombre_usuario] += self.jugador.score
            else:
                dicccionario_score[self.nombre_usuario] = self.jugador.score
            guarda_json(path, dicccionario_score)
            self.datos_guardados = True

    def dibujar_plataformas(self, evento):  
        if evento.key == pygame.K_TAB:
            # print("hola")

            # if get_mode() == True:
            for plataforma in self.plataformas:
                for lado in plataforma.lados:
                    pygame.draw.rect(self.slave,"Blue",plataforma.lados[lado] ,2)

            for bala in self.balas_personaje:
                pygame.draw.rect(self.slave,"Blue",bala.rectangulo,2)

            for lado in self.jugador.lados:
                pygame.draw.rect(self.slave,"Blue",self.jugador.lados[lado],2)

            for enemigo in self.enemigos:
                for lado in enemigo.lados:
                    pygame.draw.rect(self.slave,"Blue",enemigo.lados[lado] ,2)

