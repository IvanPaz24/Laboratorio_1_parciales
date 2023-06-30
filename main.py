from configuraciones import *
import pygame, sys
from pygame.locals import *
from class_personaje import Personaje
from class_plataforma import Plataforma
from class_proyectil import Proyectil
from class_enemigo import Enemigo
DEBUG = False  
def cambiar_modo():     
    global DEBUG     
    DEBUG = not DEBUG  

def get_mode():     
    return DEBUG

def actualizar_pantalla(pantalla, una_personaje:Personaje, fondo, lista_plataforma, balas:Proyectil, bala_enemigo,lista_enemigo):
    pantalla.blit(fondo, (0,0))
    una_personaje.update(pantalla, lista_plataforma)
    for enemigo in lista_enemigo:
        if enemigo.rectangulo.x > LARGO/2:
            enemigo.animar(pantalla, "quieto_enemigo")
        else:
            enemigo.animar(pantalla, "quieto_enemigo_derecha")
        # enemigo.animar(pantalla, "quieto_enemigo_derecha")
    
    # enemigo.update(pantalla, lista_plataforma)
    for bala in balas:
        bala.animar(pantalla)
        # enemigo.muerto(bala)
    
    for bala in bala_enemigo:
        bala.animar(pantalla)
    

#########################################################################
LARGO = 1900
ALTO = 900
TAMAÑO_PANTALLA = (LARGO,ALTO)
FPS = 15

pygame.init()

fuente = pygame.font.SysFont("Arial",60)

PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)#pixeles
pygame.display.set_caption("Metal Slug")

fondo = pygame.image.load("Mis recursos/mi_fondo.png")
fondo = pygame.transform.scale(fondo, TAMAÑO_PANTALLA)

#personaje
diccionario_animaciones = {}
diccionario_animaciones["quieto"] = personaje_quieto
diccionario_animaciones["quieto_izquierda"] = personaje_quieto_izquierda
diccionario_animaciones["salta"] = personaje_salta
diccionario_animaciones["salta_izquierda"] = personaje_salta_izquierda
diccionario_animaciones["camina_derecha"] = personaje_camina
diccionario_animaciones["camina_izquierda"] = personaje_camina_izquierda
diccionario_animaciones["golpe"] = personaje_golpe
diccionario_animaciones["golpe_izquierda"] = personaje_golpe_izquierda

#enemigo animaciones
diccionario_animaciones_enemigo = {}
diccionario_animaciones_enemigo["quieto_enemigo"] = enemigo_quieto
diccionario_animaciones_enemigo["quieto_enemigo_derecha"] = enemigo_quieto_derecha

#personaje
posicion_inicial = (LARGO/2 -300,700)
tamaño = (110, 120)
velocidad = 15
donde_mira = False
mi_personaje = Personaje(tamaño, diccionario_animaciones, posicion_inicial, velocidad, donde_mira, TAMAÑO_PANTALLA)
score = 0


#proyectil
turno_proyectiles = 0
balas = []
balas_enemigo = []
contador_balas_enemigo = 0

#piso
mi_piso = Plataforma(0,0,LARGO,20)
mi_piso.rectangulo.top = mi_personaje.lados["main"].bottom                           
mi_piso.crear_lados()

#plataforma
primer_plataforma = Plataforma(845,457,345,45)
primer_plataforma.crear_lados()

segunda_plataforma = Plataforma(843,648,160,45)
segunda_plataforma.crear_lados()

tercer_plataforma = Plataforma(1354, 460 ,330, 45)
tercer_plataforma.crear_lados()

cuarta_plataforma = Plataforma(1520, 645, 162, 45)
cuarta_plataforma.crear_lados()

lista_plataforma = [mi_piso.lados, primer_plataforma.lados, segunda_plataforma.lados,
                    tercer_plataforma.lados, cuarta_plataforma.lados]

#class enemigo
primer_enemigo = Enemigo((LARGO/2 + 300,700),(150, 120),diccionario_animaciones_enemigo)
segundo_enemigo = Enemigo((1354, 340),(150, 120),diccionario_animaciones_enemigo)
tercer_enemigo = Enemigo((LARGO/2 - 700,700),(150, 120),diccionario_animaciones_enemigo)

lista_enemigos = [primer_enemigo, segundo_enemigo, tercer_enemigo]

clock = pygame.time.Clock() 
while True:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()
    # mouse_pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()

    if turno_proyectiles > 0:
        turno_proyectiles += 1
    if turno_proyectiles > 3:
        turno_proyectiles = 0

    for bala_enemigo in balas_enemigo:
        if mi_personaje.muerto(bala_enemigo, LARGO, PANTALLA):
            balas_enemigo.pop(balas_enemigo.index(bala_enemigo))
            score -= 100

        if bala_enemigo.rectangulo.x < LARGO and bala_enemigo.rectangulo.x > 0:
            bala_enemigo.rectangulo.x += bala_enemigo.velocidad
        else:
            balas_enemigo.pop(balas_enemigo.index(bala_enemigo)) 
    
    for enemigo in lista_enemigos:
        for bala in balas:
            if enemigo.muerto(bala, lista_enemigos):
                balas.pop(balas.index(bala))
                score += 100

            if bala.rectangulo.x < LARGO and bala.rectangulo.x > 0:
                bala.rectangulo.x += bala.velocidad
            else:
                balas.pop(balas.index(bala)) 
    if keys[pygame.K_RIGHT]:
            mi_personaje.que_hace = "derecha"
            mi_personaje.donde_mira = False
    elif keys[pygame.K_LEFT]:
        mi_personaje.que_hace = "izquierda"
        mi_personaje.donde_mira = True
    elif keys[pygame.K_UP]:
        if mi_personaje.donde_mira == False:
            mi_personaje.que_hace = "salta"
        else:
            mi_personaje.que_hace = "salta_izquierda"
    elif keys[pygame.K_f]:
        if mi_personaje.donde_mira == False:
            mi_personaje.que_hace = "golpe"
            mi_personaje.golpea(lista_enemigos)
        else:
            mi_personaje.que_hace = "golpe_izquierda"
            mi_personaje.golpea(lista_enemigos)
    elif mouse[0] and turno_proyectiles == 0:
        if mi_personaje.donde_mira == False:
            direccion = 1
        elif mi_personaje.donde_mira == True:
            direccion = -1
        else:
            direccion = 0

        if len(balas) < 4:
            balas.append(Proyectil((20,20),mi_personaje.rectangulo.centerx, mi_personaje.rectangulo.centery, 45, direccion))
        turno_proyectiles = 1
    else:
        if mi_personaje.donde_mira == False:
            mi_personaje.que_hace = "quieto"
        else:
            mi_personaje.que_hace = "quieto_izquierda"
    
    contador_balas_enemigo += 1
    
    if contador_balas_enemigo == 100:
        for enemigo in lista_enemigos:
            if enemigo.rectangulo.x > LARGO/2:
                direccion_enemigo = -1
            elif enemigo.rectangulo.x < LARGO:
                direccion_enemigo = 1

            if len(balas) < 1:
                balas_enemigo.append(Proyectil((20,20), enemigo.rectangulo.centerx, enemigo.rectangulo.centery, 45, direccion_enemigo))
            turno_proyectiles = 1
            contador_balas_enemigo = 0

    actualizar_pantalla(PANTALLA, mi_personaje, fondo, lista_plataforma, balas, balas_enemigo, lista_enemigos)
    # PANTALLA.blit((0,0), primer_enemigo.rectangulo)
    # for i in range(len(mi_enemigo.animaciones["quieto_enemigo"])): 
    # for clave in mi_enemigo.animaciones:        
    #     PANTALLA.blit(mi_enemigo.animaciones[clave], mi_enemigo.rectangulo)
    # mi_enemigo.animar(PANTALLA, "quieto_enemigo")
    texto = fuente.render(f"Score {score}",False, "Green", "Blue")
    PANTALLA.blit(texto,(0,0))
    
    if get_mode():
        for lado in mi_piso.lados:
            pygame.draw.rect(PANTALLA,"Blue", mi_piso.lados[lado],2)

        for bala in balas:
            pygame.draw.rect(PANTALLA,"Blue",bala.rectangulo,2)

        for lado in mi_personaje.lados:
            pygame.draw.rect(PANTALLA,"Blue",mi_personaje.lados[lado],2)

        pygame.draw.rect(PANTALLA,"Red",primer_plataforma.rectangulo,2)
        pygame.draw.rect(PANTALLA,"Red",segunda_plataforma.rectangulo,2)
        pygame.draw.rect(PANTALLA,"Red",tercer_plataforma.rectangulo,2)
        pygame.draw.rect(PANTALLA,"Red",cuarta_plataforma.rectangulo,2)
        pygame.draw.rect(PANTALLA,"Red",primer_enemigo.rectangulo,2)

    pygame.display.update()