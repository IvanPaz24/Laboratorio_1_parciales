import pygame
from pygame.locals import *

from GUI_button import *
from GUI_slider import *
from GUI_textbox import *
from GUI_label import *
from GUI_form import *
from GUI_button_image import *
from GUI_form_score import *
from GUI_form_play import *
from configuraciones import *
import json
import sqlite3

class Form_Principal(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border = "Black", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.volumen = 0.2
        self.flag_play = True
        self.manejador_niveles = Manejador_niveles(self._master)
        self.flag_ingreso_nombre = False
        pygame.mixer.init()

        ##### Controles
        self.btn_play = Button(self._slave, x, y, 100, 100, 100, 50, 
                            "Red", "Blue", self.btn_play_click, "Nombre", "Pause", font= "Verdana", 
                            font_size= 15, font_color="White")
        
        self.label_volumen = Label(self._slave, 650, 190, 100, 50,"20%", "Comic Sans", 15,"White",
                                "Mis recursos/tabla.png")
        
        self.slider_volumen = Slider(self._slave, x, y, 100,200,500,15,self.volumen, "Black", "White")
        self.btn_tabla = Button_Image(self._slave, x, y, 408, 430,50,50, "Mis recursos/boton_imagen.png", 
                                    self.btn_tabla_click, "datos_score.json")
        self.btn_jugar = Button_Image(self._slave, x, y, 350, 300,160,100, "Mis recursos/start_imagen.png", 
                                    self.btn_jugar_click, "a")

        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(self.btn_jugar)
        ####
        pygame.mixer.music.load("Mis recursos/sonidos/intro.mp3")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)

        self.render()

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)
    
    def render(self):
        self._slave.blit(self._color_background, (0,0))

    def btn_play_click(self, texto):
        if self.flag_play:
            pygame.mixer.music.pause()
            self.btn_play._color_background = "Cyan"
            self.btn_play._font_color = "Red"
            self.btn_play.set_text("Play")
        else:
            pygame.mixer.music.unpause()
            self.btn_play._color_background = "Red"
            self.btn_play._font_color = "White"
            self.btn_play.set_text("Pause")

        self.flag_play = not self.flag_play
    
    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        # self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)

    def btn_tabla_click(self, path):
        diccionario = leer_json(path)
        form_puntaje = Form_Menu_Score(self._master, 250, 25, 500,550, "Red", "White", True, 
                                    "Mis recursos/tabla score.png", diccionario,100,10,10)
        
        self.show_dialog(form_puntaje)

    def btn_jugar_click(self, param):
        frm_jugar = Form_Menu_Play(self._master, x = self._master.get_width() /2 - 250,
                                y =self._master.get_height() / 2- 250 , w = 500, h =500, color_background="Red"
                                ,color_border="White", active=True, path="Mis recursos/tabla score.png")
        # self.score = frm_jugar.score
        # print(self.score)
        self.show_dialog(frm_jugar)
