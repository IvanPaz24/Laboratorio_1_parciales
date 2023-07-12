import pygame
from pygame.locals import *

from GUI_form import *
from GUI_label import *
from GUI_button_image import *

class Form_Menu_Score(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path, score, margen_y, margen_x, espacio):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)

        aux_imagen = pygame.image.load(path)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))

        self._slave = aux_imagen
        self._score = score

        self._margen_y = margen_y

        label_jugador = Label(self._slave, x=margen_x + 10, y = 20, w=w/2-margen_x -10, h=50, text= "Jugador", font= "Verdana"
                        ,font_size= 30, font_color= "White", path_image= "Mis recursos/tabla.png")
        
        label_puntaje = Label(self._slave, x=margen_x + 10 + w/2- margen_x-10, y = 20, w=w/2-margen_x -10, h=50, text= "Puntaje", font= "Verdana"
                        ,font_size= 30, font_color= "White", path_image= "Mis recursos/tabla.png")

        self.lista_widgets.append(label_jugador)
        self.lista_widgets.append(label_puntaje)

        pos_inicial_y = margen_y
        pos_inicial_x = margen_x
        for k,v in self._score.items():
            label_jugador_actual = Label(self._slave, margen_x, pos_inicial_y, w/2-margen_x, 100, k, "Verdana",
                                        30, "White", "Mis recursos/tabla.png")
            label_puntaje_actual = Label(self._slave, pos_inicial_x + (w/2 - margen_x), pos_inicial_y, w/2-margen_x, 100, str(v), "Verdana",
                                        30, "White", "Mis recursos/tabla.png")
            self.lista_widgets.append(label_jugador_actual)
            self.lista_widgets.append(label_puntaje_actual)
            
            pos_inicial_y += 100 + espacio

        self._btn_home = Button_Image(screen=self._slave, x = w-70, y = h-70, master_x = x, master_y= y, w = 50, h = 50,
                                    color_background= "Black", color_border= "White", onclick= self.btn_home_click, onclick_param= "",
                                    text = "", font= "Verdanda", font_size= 15, font_color= "White",path_image= "Mis recursos/home.png")

        self.lista_widgets.append(self._btn_home)

    def btn_home_click(self, param):
        self.end_dialog()

    def update(self, lista_eventos):
        if self.active:
            for wid in self.lista_widgets:
                wid.update(lista_eventos)
            self.draw()
