import pygame
from class_patrulla import Patraulla

'''
El constructor de la clase Jefe que inicializa un objeto Jefe. 
Recibe tres parámetros: posicion (la posición inicial del jefe), tamaño (el tamaño del jefe) 
y animaciones (las animaciones del jefe). 
Establece el atributo vida del jefe en 10 llamando al constructor de la clase base Patrulla usando super().__init__().
'''
class Jefe(Patraulla):
    def __init__(self, posicion, tamaño, animaciones):
        super().__init__(posicion, tamaño, animaciones)
        self.vida = 10
    
    '''
    Método que redimensiona las animaciones del jefe. 
    Llama al método reescalar_animaciones() de la clase base Patrulla usando super().reescalar_animaciones().
    '''
    def reescalar_animaciones(self):
        return super().reescalar_animaciones()
    '''
    Método que muestra una animación específica en la pantalla. 
    Llama al método animar() de la clase base Patrulla usando super().animar().
    '''
    def animar(self, pantalla, que_animacion):
        return super().animar(pantalla, que_animacion)
    '''
    Método que controla el movimiento del jefe en la pantalla. 
    Renderiza la vida actual del jefe en la pantalla y 
    luego llama al método se_mueve() de la clase base Patrulla usando super().se_mueve().
    '''
    def se_mueve(self, pantalla, lista_plataforma, fuente):
        vida_actual = fuente.render(f"Jefe:{self.vida}",False, "Red")
        pantalla.blit(vida_actual, (1690, 100))
        return super().se_mueve(pantalla, lista_plataforma)
    '''
    Método que verifica si el jefe colisiona con alguna plataforma. 
    Llama al método coliciona_plataforma() de la clase base Patrulla usando super().coliciona_plataforma().
    '''
    def coliciona_plataforma(self, lista_plataforma):
        return super().coliciona_plataforma(lista_plataforma)
    '''
    Método que verifica si el jefe ha sido golpeado por un proyectil y está muerto. 
    Devuelve un valor booleano indicando si el jefe está muerto o no.
    '''
    def muerto(self, proyectil, lista_enemigos):
        flag = False
        if proyectil.rectangulo.colliderect(self.rectangulo):
            flag = True
        return flag
    '''
    Método que hace que el jefe desaparezca de la lista de enemigos si su vida es menor a 1.
    '''
    def desaparecer_personaje(self, lista_enemigo:list):
        if self.vida < 1:
            lista_enemigo.remove(self)
    '''
    Método que maneja la colisión entre las balas y el jefe, y actualiza el puntaje del personaje. 
    También verifica si el jefe está muerto y lo elimina de la lista de enemigos. 
    Además, maneja la eliminación de las balas que colisionan con las plataformas.
    '''
    def bala_colision(self, largo,lista_balas, lista_enemigos, personaje, lista_plataforma):
        for bala in lista_balas:
            if self.muerto(bala, lista_enemigos):
                lista_balas.pop(lista_balas.index(bala))
                personaje.score += 100
                self.vida -= 1 
                self.desaparecer_personaje(lista_enemigos)

            if bala.rectangulo.x < largo and bala.rectangulo.x > 0:
                bala.rectangulo.x += bala.velocidad
            else:
                lista_balas.pop(lista_balas.index(bala)) 

            for plataforma in lista_plataforma:
                if bala.rectangulo.colliderect(plataforma.lados["main"]):
                    lista_balas.pop(lista_balas.index(bala))
