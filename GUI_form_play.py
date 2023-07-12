from GUI_form import *
from GUI_label import *
from GUI_button_image import *
from class_manejador_niveles import *
from GUI_form_contendor_niveles import *
from GUI_textbox import *

class Form_Menu_Play(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
        self.manejador_niveles = Manejador_niveles(self._master)
        aux_imagen = pygame.image.load(path)
        aux_imagen = pygame.transform.scale(aux_imagen, (w,h))
        # self.nivel = None
        # self.frm_contenedor_nivel = Form_Contenedor_Niveles
        self.score = 0
        
        self._slave = aux_imagen

        self.txtbox = TextBox(self._slave, x, y, 50, 50, 150, 30, 
                            "Gray","White", "Red", "Blue", 2, font = "Comic sans", font_size = 15, font_color= "Black" )
        
        self._btn_level_1 = Button_Image(screen=self._slave, x = 100, y = 100, master_x = x, master_y= y, w = 100, h = 150,
                                    onclick= self.entrar_nivel, onclick_param= "nivel_uno",path_image= "Mis recursos/imagen_nivel_1.png")

        self._btn_level_2 = Button_Image(screen=self._slave, x = 250, y = 100, master_x = x, master_y= y, w = 100, h = 150,
                                    onclick= self.entrar_nivel, onclick_param= "nivel_dos",path_image= "Mis recursos/imagen_nivel_2.png")
        
        self._btn_level_3 = Button_Image(screen=self._slave, x = 100, y = 270, master_x = x, master_y= y, w = 100, h = 150,
                                    onclick= self.entrar_nivel, onclick_param= "nivel_tres",path_image= "Mis recursos/imagen_nivel_3.png")
        
        self._btn_home = Button_Image(screen=self._slave, x = w-70, y = h-70, master_x = x, master_y= y, w = 50, h = 50,
                                    color_background= "Black", color_border= "White", onclick= self.btn_home_click, onclick_param= "",
                                    text = "", font= "Verdanda", font_size= 15, font_color= "White",path_image= "Mis recursos/home.png")
        
        self.lista_widgets.append(self._btn_level_1)
        self.lista_widgets.append(self._btn_level_2)
        self.lista_widgets.append(self._btn_level_3)
        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(self.txtbox)

    def on(self, parametro):
        print("hola", parametro)
    
    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)

    def entrar_nivel(self, nombre_nivel):
        if len(self.txtbox.get_text()) == 0:
            nivel = self.manejador_niveles.get_nivel(nombre_nivel, "user")
        else:
            nivel = self.manejador_niveles.get_nivel(nombre_nivel, self.txtbox.get_text())
        # except:
            
        frm_contenedor_nivel = Form_Contenedor_Niveles(self._master, nivel)
        self.show_dialog(frm_contenedor_nivel)
    
    def btn_home_click(self, param):
        self.end_dialog()

    