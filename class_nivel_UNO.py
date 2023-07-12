from configuraciones import *
import pygame, sys
from pygame.locals import *
from class_personaje import Personaje
from class_plataforma import Plataforma
from class_proyectil import Proyectil
from class_enemigo import Enemigo
from class_item import Item
from class_nivel import Nivel
from class_trampa import Trampa

'''
Recibe la pantalla donde se mostrará el nivel (pantalla) y el nombre del usuario (nombre_usuario). 
Configura el tamaño de la pantalla y el título del juego. Carga la imagen de fondo del nivel. 
Crea un diccionario de animaciones para el personaje y los enemigos. Establece la posición inicial, 
tamaño, velocidad y dirección del personaje. Crea las instancias de las plataformas, el piso y los enemigos. 
Llama al constructor de la clase Nivel pasando los parámetros correspondientes.
'''
class Nivel_Uno(Nivel):
    def __init__(self, pantalla, nombre_usuario):
        LARGO = pantalla.get_width()
        ALTO = pantalla.get_height()

        fuente = pygame.font.SysFont("Arial",60)

        pantalla = pygame.display.set_mode((LARGO,ALTO))#pixeles
        pygame.display.set_caption("Metal Slug")

        fondo = pygame.image.load("Mis recursos/mi_fondo.png")
        fondo = pygame.transform.scale(fondo, (LARGO,ALTO))

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
        mi_personaje = Personaje(tamaño, diccionario_animaciones, posicion_inicial, velocidad, donde_mira, (LARGO,ALTO))


        #proyectil
        balas = []
        balas_enemigo = []

        #piso
        mi_piso = Plataforma(0,0,LARGO,20)
        mi_piso.rectangulo.top = mi_personaje.lados["main"].bottom                           
        mi_piso.crear_lados()

        #plataforma
        primer_plataforma = Plataforma(845,457,345,45)
        primer_plataforma.crear_lados()

        segunda_plataforma = Plataforma(843,648,160,30)
        segunda_plataforma.crear_lados()

        tercer_plataforma = Plataforma(1354, 460 ,330, 45)
        tercer_plataforma.crear_lados()

        cuarta_plataforma = Plataforma(1520, 645, 162, 30)
        cuarta_plataforma.crear_lados()

        lista_plataforma = [mi_piso, primer_plataforma, segunda_plataforma,
                            tercer_plataforma, cuarta_plataforma]

        mi_item = Item(item,(LARGO/2 + 300, mi_piso.lados["top"].top - 50),(50, 50))
        mi_otro_item = Item(item,(LARGO/2 + 50, 410),(50, 50))
        lista_items = [mi_item, mi_otro_item]

        primer_enemigo = Enemigo((LARGO/2 + 300,700),(150, 120),diccionario_animaciones_enemigo)
        segundo_enemigo = Enemigo((1354, 340),(150, 120),diccionario_animaciones_enemigo)
        tercer_enemigo = Enemigo((LARGO/2 - 700,700),(150, 120),diccionario_animaciones_enemigo)

        lista_enemigos = [primer_enemigo, segundo_enemigo, tercer_enemigo]

        contador_nivel = 6
        trampa = Trampa((150, 100), LARGO/2 +100, mi_piso.lados["top"].top - 100)

        super().__init__(pantalla, mi_personaje, lista_plataforma, fondo, lista_enemigos, LARGO, 
                        balas, balas_enemigo, lista_items, fuente,contador_nivel, trampa, nombre_usuario)