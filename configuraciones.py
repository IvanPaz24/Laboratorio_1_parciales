import pygame
import json
from configuraciones import *
'''
Este método recibe una lista de imágenes y un tamaño y redimensiona todas las imágenes de la lista al tamaño especificado 
utilizando la función pygame.transform.scale().
'''
def reescalar_imagenes(lista_imagenes, tamaño):
    for i in range(len(lista_imagenes)):
        lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i], tamaño)
'''
Este método recibe una lista de imágenes y un tamaño y redimensiona todas las imágenes de la lista al 
tamaño especificado utilizando la función pygame.transform.scale().
'''
def girar_imagenes(lista,flip_x,flip_y):
    lista_girada = []
    for imagen in lista:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))

    return lista_girada
'''
Este método recibe un rectángulo principal y devuelve un diccionario que contiene diferentes 
rectángulos correspondientes a los lados del rectángulo principal. 
Los rectángulos se denominan "main", "bottom", "right", "left" y "top" y se crean utilizando la clase pygame.Rect.
'''
def obtener_rectangulos(principal):
    diccionario = {}

    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom- 10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right - 10, principal.top, 2, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top,10 , principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)

    return diccionario

personaje_quieto = [pygame.image.load("Mis recursos/quieto/0.png"),
                    pygame.image.load("Mis recursos/quieto/1.png"),
                    pygame.image.load("Mis recursos/quieto/2.png"),
                    pygame.image.load("Mis recursos/quieto/3.png"),
                    pygame.image.load("Mis recursos/quieto/4.png")] 

personaje_quieto_izquierda = girar_imagenes(personaje_quieto, True, False)

personaje_camina = [pygame.image.load("Mis recursos/camina/0.png"),
                    pygame.image.load("Mis recursos/camina/2.png"),
                    pygame.image.load("Mis recursos/camina/5.png"),
                    pygame.image.load("Mis recursos/camina/6.png"),
                    pygame.image.load("Mis recursos/camina/7.png"),
                    pygame.image.load("Mis recursos/camina/8.png"),
                    pygame.image.load("Mis recursos/camina/9.png"),
                    pygame.image.load("Mis recursos/camina/10.png"),
                    pygame.image.load("Mis recursos/camina/11.png"),
                    pygame.image.load("Mis recursos/camina/12.png"),
                    pygame.image.load("Mis recursos/camina/13.png")]

personaje_camina_izquierda = girar_imagenes(personaje_camina, True, False)

personaje_salta = [pygame.image.load("Mis recursos/salta/67.png")]


personaje_salta_izquierda = girar_imagenes(personaje_salta, True, False)

personaje_golpe = [pygame.image.load("Mis recursos/golpe/0.png"),
                pygame.image.load("Mis recursos/golpe/0.png"),
                pygame.image.load("Mis recursos/golpe/0.png"),
                pygame.image.load("Mis recursos/golpe/0.png"),
                    pygame.image.load("Mis recursos/golpe/0.png"),
                    pygame.image.load("Mis recursos/golpe/0.png"),
                    pygame.image.load("Mis recursos/golpe/0.png"),
                    pygame.image.load("Mis recursos/golpe/0.png"),
                    pygame.image.load("Mis recursos/golpe/1.png"),
                    pygame.image.load("Mis recursos/golpe/1.png"),
                    pygame.image.load("Mis recursos/golpe/1.png"),
                    pygame.image.load("Mis recursos/golpe/1.png"),
                    pygame.image.load("Mis recursos/golpe/1.png"),
                    pygame.image.load("Mis recursos/golpe/5.png"),
                    pygame.image.load("Mis recursos/golpe/5.png"),
                    pygame.image.load("Mis recursos/golpe/5.png"),
                    pygame.image.load("Mis recursos/golpe/5.png"),
                    pygame.image.load("Mis recursos/golpe/5.png"),
                    pygame.image.load("Mis recursos/golpe/6.png"),
                    pygame.image.load("Mis recursos/golpe/6.png"),
                    pygame.image.load("Mis recursos/golpe/6.png"),
                    pygame.image.load("Mis recursos/golpe/6.png"),
                    pygame.image.load("Mis recursos/golpe/6.png"),
                    pygame.image.load("Mis recursos/golpe/7.png")]

personaje_golpe_izquierda = girar_imagenes(personaje_golpe, True, False)

proyectil = pygame.image.load("Mis recursos/proyectil/1.png")

enemigo_quieto = [pygame.image.load("Mis recursos/enemigo/0.png"),
                pygame.image.load("Mis recursos/enemigo/0.png"),
                pygame.image.load("Mis recursos/enemigo/0.png"),
                pygame.image.load("Mis recursos/enemigo/1.png"),
                pygame.image.load("Mis recursos/enemigo/1.png"),
                pygame.image.load("Mis recursos/enemigo/1.png"),
                pygame.image.load("Mis recursos/enemigo/2.png"),
                pygame.image.load("Mis recursos/enemigo/2.png"),
                pygame.image.load("Mis recursos/enemigo/2.png"),] 

enemigo_quieto_derecha = girar_imagenes(enemigo_quieto,True,False)

patraulla_izquierda = [pygame.image.load("Mis recursos/patrulla/4.png"),
                        pygame.image.load("Mis recursos/patrulla/5.png"),
                        pygame.image.load("Mis recursos/patrulla/6.png"),
                        pygame.image.load("Mis recursos/patrulla/7.png"),
                        pygame.image.load("Mis recursos/patrulla/8.png"),
                        pygame.image.load("Mis recursos/patrulla/9.png"),
                        pygame.image.load("Mis recursos/patrulla/10.png")]

patraulla_derecha = girar_imagenes(patraulla_izquierda, True, False)

item = pygame.image.load("Mis recursos/0.png")

trampa_imagen = pygame.image.load("Mis recursos/trampa/trampa.png")

jefe_final_izquierda = [pygame.image.load("Mis recursos/boss/0.png"),
            pygame.image.load("Mis recursos/boss/1.png"),
            pygame.image.load("Mis recursos/boss/2.png"),
            pygame.image.load("Mis recursos/boss/3.png"),
            pygame.image.load("Mis recursos/boss/4.png"),
            pygame.image.load("Mis recursos/boss/5.png"),
            pygame.image.load("Mis recursos/boss/6.png"),
            pygame.image.load("Mis recursos/boss/7.png"),
            pygame.image.load("Mis recursos/boss/8.png"),
            pygame.image.load("Mis recursos/boss/9.png")]

jefe_final_derecha = girar_imagenes(jefe_final_izquierda, True, False)

'''
Guarda un diccionario en formato JSON en un archivo especificado.

    Parámetros:
        path (str): Ruta del archivo donde se guardará el diccionario.
        diccionario (dict): Diccionario a guardar en formato JSON.
'''
def guarda_json(path, dicccionario):
    # for datos in dicccionario:
    with open(path, "w") as archivo:
        json.dump(dicccionario, archivo, indent= 4)

'''
Guarda un diccionario en formato JSON en un archivo especificado.

    Parámetros:
        path (str): Ruta del archivo donde se guardará el diccionario.
        diccionario (dict): Diccionario a guardar en formato JSON.
'''
def leer_json(path):
    try:
        with open(path, "r") as mi_archivo:
                lectura = json.load(mi_archivo)
                
        return lectura
    except:
        return {}
