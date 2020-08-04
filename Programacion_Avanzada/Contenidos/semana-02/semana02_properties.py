class Auto:
    def __init__(self,ma,mo,a,c,k): #atributos de instancias
        self.marca=ma
        self.modelo=mo
        self.año=a
        self.color=c
        self.__kilometraje=k
        self.__ubicacion = (-33.45,-70.63)
        self.dueño=None

#para modificar atributos privados, se utilizan metodos especificos
    def get_kilometraje(): ##getter
        return self.__kilometraje

    def set_kilometraje(kms): ##setter
        self.__kilometraje=kms

    def conducir (self,kms): #self -> instancias se refieren a si misma
        self.__kilometraje+=kms
        self.__modificar_ubicacion()

    def vender(self,nuevo_dueño):
        self.dueño=nuevo_dueño

    def leer_odometro(self):
        return self.__kilometraje

    def __modificar_ubicacion(self):
        print("Calcular nueva ubicacion:")
        self._ubicacion=(self._ubicacion[0]+0.01,self._ubicacion[1]-0.01)

#alternativa a getter y setter: Property
#permite facilitar el encapsulamiento de atributos

class Puente:
    def __init__(self,maximo):
        self.maximo=maximo
        self.__personas=0
    def contar(self): #getter: permite obtener atributo
        return self.__personas #se ahorra incluir tedio de variable privada __
    def ingresar(self,p): #setter: permite actualizar atributo
        if self.__personas+p > self.maximo:
            self.__personas=self.maximo
        elif self.__personas+p <0:
            self.__personas=0
        else:
            self.__personas+=p

puente=Puente(10)
puente.ingresar(7)
print(f'Hay {puente.contar()} personas en el puente')
puente.ingresar(5)
print(f'Hay {puente.contar()} personas en el puente')
puente.ingresar(-15)
print(f'Hay {puente.contar()} personas en el puente')

#property, decorador que realiza mismo comportamiento
class Puente_p:
    def __init__(self,maximo):
        self.maximo=maximo
        self.__personas=0
    @property
    def personas(self):
        return self.__personas
    @personas.setter #permite asociar metodos distintos para misma variable
    def personas(self,p): #setter: permite actualizar atributo
        if p > self.maximo:
            self.__personas=self.maximo
        elif p <0:
            self.__personas=0
        else:
            self.__personas=p

puente2=Puente_p(10)
puente2.personas+=7 #actua como variable
print(f'Hay {puente2.personas} personas en el puente2')
puente2.personas+=5
print(f'Hay {puente2.personas} personas en el puente2')
puente2.personas-=15
print(f'Hay {puente2.personas} personas en el puente2')

class Email:
    def __init__(self,address):
        self.__email=address
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,value):
        if '@' not in value:
            print("Esto no es una direccion de correo")
        else:
            self.__email=value
    @email.deleter
    def email(self):
        print("Eliminaste el correo")
        del self.__email

mail=Email("diegoaldunatec@gmail.com")
print(mail.email)
mail.email="Daaldunate@uc.cl"
print(mail.email)
mail.email="da.com"
print(mail.email)
del mail.email #deleter de property