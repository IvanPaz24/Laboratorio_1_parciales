import pygame
import sys
from GUI_form_principal import *
DEBUG = False  
def cambiar_modo():     
    global DEBUG     
    DEBUG = not DEBUG  

def get_mode():     
    return DEBUG

pygame.init()

LARGO = 1900
ALTO = 900
TAMAÑO_PANTALLA = (LARGO,ALTO)
FPS = 13

reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode((TAMAÑO_PANTALLA))
fondo = pygame.image.load("Mis recursos/fondo_menu.jpg")
fondo = pygame.transform.scale(fondo, (TAMAÑO_PANTALLA))

form_prueba = Form_Principal(pantalla, 550, 200, 900, 600, fondo, "White", 5, True)

while True:
    reloj.tick(FPS)
    eventos = pygame.event.get()
    pantalla.fill("Black")
    for event in eventos:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    form_prueba.update(eventos)

    # if get_mode():
    #     for plataforma in nivel_actual.plataformas:
    #         for lado in plataforma.lados:
    #             pygame.draw.rect(PANTALLA,"Blue",plataforma.lados[lado] ,2)

    #     for bala in nivel_actual.balas_personaje:
    #         pygame.draw.rect(PANTALLA,"Blue",bala.rectangulo,2)

    #     for lado in nivel_actual.jugador.lados:
    #         pygame.draw.rect(PANTALLA,"Blue",nivel_actual.jugador.lados[lado],2)

    #     for enemigo in nivel_actual.enemigos:
    #         for lado in enemigo.lados:
    #             pygame.draw.rect(PANTALLA,"Blue",enemigo.lados[lado] ,2)
    pygame.display.flip()