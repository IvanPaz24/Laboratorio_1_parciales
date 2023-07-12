from pygame.locals import *
from class_nivel_UNO import *
from class_nivel_DOS import *
from class_nivel_TRES import *

class Manejador_niveles:
    def __init__(self, pantalla):
        self._slave = pantalla
        self.niveles = {"nivel_uno": Nivel_Uno, "nivel_dos": Nivel_Dos, "nivel_tres": Nivel_Tres}

    def get_nivel(self, nombre_nivel, nombre_usuario):
        return self.niveles[nombre_nivel](self._slave, nombre_usuario)
    