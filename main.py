from configuraciones import *
import pygame, sys
from pygame.locals import *
from class_personaje import Personaje
from class_plataforma import Plataforma
from class_proyectil import Proyectil
from class_enemigo import Enemigo
from class_item import Item
from class_nivel_UNO import Nivel_Uno
from class_nivel_DOS import Nivel_Dos
# from cabiar_modo import *
DEBUG = False  
def cambiar_modo():     
    global DEBUG     
    DEBUG = not DEBUG  

def get_mode():     
    return DEBUG

LARGO = 1900
ALTO = 900
TAMAÑO_PANTALLA = (LARGO,ALTO)
FPS = 13

pygame.init()

PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)#pixeles
pygame.display.set_caption("Metal Slug")

clock = pygame.time.Clock() 

nivel_actual = Nivel_Dos(PANTALLA)
while True:
    clock.tick(FPS)
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()

    nivel_actual.update(eventos)

    # PANTALLA.blit(nivel_actual.plataformas[1].imagen, nivel_actual.plataformas[1].rectangulo)

    # if mi_personaje.vida < 1 or contador_nivel < 0:
    #     # minutos = 0
    #     # segundos = 0
    #     PANTALLA.blit(game_over,(0,0))

    
    if get_mode():
        for plataforma in nivel_actual.plataformas:
            for lado in plataforma.lados:
                pygame.draw.rect(PANTALLA,"Blue",plataforma.lados[lado] ,2)

        for bala in nivel_actual.balas_personaje:
            pygame.draw.rect(PANTALLA,"Blue",bala.rectangulo,2)

        for lado in nivel_actual.jugador.lados:
            pygame.draw.rect(PANTALLA,"Blue",nivel_actual.jugador.lados[lado],2)

        # pygame.draw.rect(PANTALLA,"Red",primer_plataforma.rectangulo,2)
        # pygame.draw.rect(PANTALLA,"Red",segunda_plataforma.rectangulo,2)
        # pygame.draw.rect(PANTALLA,"Red",tercer_plataforma.rectangulo,2)
        # pygame.draw.rect(PANTALLA,"Red",cuarta_plataforma.rectangulo,2)
        # pygame.draw.rect(PANTALLA,"Red",primer_enemigo.rectangulo,2)

    pygame.display.update()