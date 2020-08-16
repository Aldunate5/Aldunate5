# Para un problema macro, es util definir a priori un diagrama que explica las clases y las relaciones entre ellas
#Clases: Encapsulan informacion
#Relaciones: Interaccion entre las distintas clases
    #Composicion: Los objetos de una clase se incluyen dentro de otro objeto (dependen de su existencia)
    #Agregacion: Se agrega objetos de una clase a otra clase . Sin embargo, son independientes
    #Herencia: subclase hereda atributos y metodos de superclase. Puede tener caracteristicas especificas

#modelo integrado: se genera un diagrama que muestra las clases y como se relacionan entre ellos

class Juego:
    def __init__(self):
        self.timestamp_inicio = 0
        self.tiempo_actual = 0
        # Al ser relación de composición, creamos a Mario dentro de juego
        self.personaje = Mario()
        self.puntaje = 0
        # Aquí incluiremos goombas que crearemos durante la inicialización del juego
        self.goombas = list()
        # Aquí incluiremos champiñones que crearemos durante la inicialización del juego
        self.champiñones = list()
        # Aquí incluiremos ladrillos que crearemos durante la inicialización del juego
        self.ladrillos = list()

    def iniciar_juego():
        pass

    def finalizar_juego():
        pass


class Mario:
    def __init__(self):
        self.posicion_x = 0
        self.posicion_y = 0
        self.cantidad_de_vidas = 5
        # Aquí incluiremos champiñones que Mario obtendrá durante el juego
        self.poders = list()

    def avanzar():
        pass

    def retroceder():
        pass

    def saltar():
        pass

    def disparar(poder):
        pass


class Goomba:
    def __init__(self):
        self.posicion_x = 0
        self.posicion_y = 0
        self.vivo = True


class Ejercito:
    def __init__(self, lista_goombas):
        # Al ser relación de agregación, suponemos que los objetos ya están
        # creados, o bien se agregarán de manera externa al __init__
        self.goombas = lista_goombas


class Champiñon:
    def __init__(self, x, y):
        self.posicion_x = x
        self.posicion_y = y


class Ladrillo:
    def __init__(self, x, y):
        self.posicion_x = x
        self.posicion_y = y


class LadrilloMoneda(Ladrillo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.valor_moneda = 10


class LadrilloMovil(Ladrillo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.esconde_champiñon = False