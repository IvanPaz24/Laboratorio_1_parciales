import pygame

def reescalar_imagenes(lista_imagenes, tamaño):
    # for lista in lista_imagenes:
    for i in range(len(lista_imagenes)):
        lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i], tamaño)

def girar_imagenes(lista,flip_x,flip_y):
    lista_girada = []
    for imagen in lista:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))

    return lista_girada

def obtener_rectangulos(principal):
    diccionario = {}

    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom- 10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right-2, principal.top, 2, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top,2, principal.height)
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

personaje_salta = [#pygame.image.load("Mis recursos/salta/60.png"),
                #pygame.image.load("Mis recursos/salta/61.png"),
                #pygame.image.load("Mis recursos/salta/62.png"),
                #pygame.image.load("Mis recursos/salta/63.png"),
                #pygame.image.load("Mis recursos/salta/64.png"),
                #pygame.image.load("Mis recursos/salta/65.png"),
                #pygame.image.load("Mis recursos/salta/66.png"),
                pygame.image.load("Mis recursos/salta/67.png"),
                #pygame.image.load("Mis recursos/salta/68.png"),
                #pygame.image.load("Mis recursos/salta/69.png"),
                #pygame.image.load("Mis recursos/salta/70.png"),
                #pygame.image.load("Mis recursos/salta/71.png"),
                #pygame.image.load("Mis recursos/salta/72.png"),
                #pygame.image.load("Mis recursos/salta/73.png"),
]

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
                    #pygame.image.load("Mis recursos/golpe/2.png"),]
                    #pygame.image.load("Mis recursos/golpe/3.png"),]
                    #pygame.image.load("Mis recursos/golpe/4.png"),]
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
            #pygame.image.load("Mis recursos/proyectil/0.png")
# reescalar_imagenes

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

item = pygame.image.load("Mis recursos/0.png")