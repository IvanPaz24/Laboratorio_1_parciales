from class_enemigo import *
import random
'''
: El constructor de la clase Patraulla que inicializa un objeto Patraulla. 
Llama al constructor de la clase base Enemigo usando super().__init__(posicion, tamaño, animaciones). 
Además, establece los atributos velocidad, va_derecha, va_izquierda, contador_enemigo y 
direccion del objeto Patraulla.
'''
class Patraulla(Enemigo):
    def __init__(self, posicion, tamaño, animaciones):
        super().__init__(posicion, tamaño, animaciones)
        self.velocidad = 10
        self.va_derecha = True
        self.va_izquierda = False
        self.contador_enemigo = 10
        self.direccion = 0
    '''
    Método que redimensiona las animaciones de la patrulla. 
    Llama al método reescalar_animaciones() de la clase base Enemigo usando super().reescalar_animaciones().
    '''
    def reescalar_animaciones(self):
        return super().reescalar_animaciones()
    
    '''
    Método que muestra una animación específica en la pantalla. 
    Verifica si el contador de enemigo (contador_enemigo) es mayor a 3 antes de llamar al método animar() 
    de la clase base Enemigo.
    '''
    def animar(self, pantalla, que_animacion):
        if self.contador_enemigo > 3:
            super().animar(pantalla, que_animacion)
    '''
    Método que controla el movimiento de la patrulla en la pantalla. 
    Verifica si el contador de enemigo es mayor a 3. Si va_derecha es verdadero, 
    mueve la patrulla hacia la derecha y verifica si ha alcanzado el límite derecho de la pantalla. 
    Si va_izquierda es verdadero, mueve la patrulla hacia la izquierda y 
    verifica si ha alcanzado el límite izquierdo de la pantalla. Además, llama al método coliciona_plataforma() 
    para verificar la colisión con las plataformas.
    '''
    def se_mueve(self, pantalla, lista_plataforma):
        if self.contador_enemigo > 3:
            if self.va_derecha:
                nueva_x = self.rectangulo.x + 10
                if nueva_x < pantalla.get_width() - self.ancho:
                    # self.mover(self.velocidad)
                    for lado in self.lados:
                        self.lados[lado].x += self.velocidad
                    self.animar(pantalla, "quieto_enemigo_derecha")
                    self.direccion = 1
                else:
                    self.va_derecha = False
                    self.va_izquierda = True
            elif self.va_izquierda:
                nueva_x = self.rectangulo.x - 10
                if nueva_x > 0:
                    for lado in self.lados:
                            self.lados[lado].x += self.velocidad * -1
                    self.animar(pantalla, "quieto_enemigo")
                    self.direccion = -1
                else:
                    self.va_derecha = True
                    self.va_izquierda = False
            self.coliciona_plataforma(lista_plataforma)
    '''
    Método que verifica si la patrulla colisiona con alguna plataforma. 
    Compara las colisiones entre los lados derecho e izquierdo de la patrulla y los lados izquierdo 
    y derecho de las plataformas.
    '''
    def coliciona_plataforma(self, lista_plataforma):
        for plataforma in lista_plataforma:
            if self.lados["right"].colliderect(plataforma.lados["left"]):
                self.va_derecha = False
                self.va_izquierda = True
            elif self.lados["left"].colliderect(plataforma.lados["right"]):
                self.va_izquierda = False
                self.va_derecha = True
    '''
    Método que verifica si la patrulla ha sido golpeada por un proyectil y está muerta. 
    Si hay una colisión entre el rectángulo del proyectil y el rectángulo de la patrulla, 
    llama al método desaparecer_personaje() y devuelve True.
    '''
    def muerto(self, proyectil):
        if self.contador_enemigo > 3:
            flag = False
            if proyectil.rectangulo.colliderect(self.rectangulo):
                self.desaparecer_personaje()
                flag = True

                return flag
    '''
    Método que hace que la patrulla desaparezca cambiando su posición a una posición aleatoria. 
    Utiliza el método obtener_rectangulos() para obtener los rectángulos correspondientes a la nueva posición.
    '''
    def desaparecer_personaje(self):
            posicion_aleatoria = random.randint(1, 1000)
            for lado in self.lados:
                self.lados[lado].x = posicion_aleatoria
            self.lados = obtener_rectangulos(self.rectangulo)
    '''
    Método que maneja la colisión entre las balas y la patrulla, actualiza el puntaje del personaje y 
    decrementa el contador de enemigo (contador_enemigo). Además, elimina las balas que colisionan con las plataformas.
    '''
    def bala_colision(self, largo,lista_balas, personaje, lista_plataforma):
        if self.contador_enemigo > 3:
            for bala in lista_balas:
                if self.muerto(bala):
                    lista_balas.pop(lista_balas.index(bala))
                    personaje.score += 100
                    self.contador_enemigo -= 1

                if bala.rectangulo.x < largo and bala.rectangulo.x > 0:
                    bala.rectangulo.x += bala.velocidad
                else:
                    lista_balas.pop(lista_balas.index(bala)) 

                for plataforma in lista_plataforma:
                        if bala.rectangulo.colliderect(plataforma.lados["main"]):
                            lista_balas.pop(lista_balas.index(bala))
