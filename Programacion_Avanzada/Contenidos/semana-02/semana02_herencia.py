class Auto:
    def __init__(self,ma,mo,a,c,k): #atributos de instancias
        self.marca=ma
        self.modelo=mo
        self.año=a
        self.color=c
        self.__kilometraje=k
        self._ubicacion = (-33.45,-70.63)
        self.dueño=None

    def conducir (self,kms): #self -> instancias se refieren a si misma
        self.__kilometraje+=kms
        self.modificar_ubicacion()
        print(f"Conudciendo {kms}")

    def vender(self,nuevo_dueño):
        self.dueño=nuevo_dueño

    def leer_odometro(self):
        return self.__kilometraje

    def modificar_ubicacion(self):
        print("Calcular nueva ubicacion:")
        self._ubicacion=(self._ubicacion[0]+0.01,self._ubicacion[1]-0.01)

class FurgonEscolar(Auto): #se hereda clase madre
    def __init__(self,marca,modelo,ano,color,kms):
        Auto.__init__(self,marca,modelo,ano,color,kms) #se llama __init__ de clase madre;
        #super().__init__(marca,modelo,ano,color,kms)# utilizar super() para facilidad, entendible; no utiliza self
        self.ninos_y_ninas=[]

    def inscribir(self,nino_o_nina):
        self.ninos_y_ninas.append(nino_o_nina)

    def conducir(self,kms): #override de metodo de superclase
        print(f'Ninos implica mayor cuidado: {kms}')

auto=Auto("Kia","Sportage",2000,"Blanco",134000)
furgon=FurgonEscolar("Kia","Sportage",2000,"Blanco",135000)
print(f'Marca: {furgon.marca}, Modelo:{furgon.modelo}, Color: {furgon.color}')
furgon.conducir(5)
print(f'Kilometraje: {furgon.leer_odometro()}')
furgon.inscribir("Benjamin")
furgon.inscribir("Enzo")
furgon.inscribir("Daniela")
print(f'Lista de Ninos: {furgon.ninos_y_ninas}')

auto.conducir(10)
furgon.conducir(10) #override de metodo de superclase

print(type(auto))
print(type(furgon))


class ContactList(list): #amplio clase lista predeterminadapara incluir metodo de busqueda)
    #para editar no realiza init de super()
    def buscar(self,nombre):
        matches=[]
        for contacto in self:
            if nombre in contacto.nombre:
                matches.append(contacto)
        return matches

class Contacto:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email

class Familiar(Contacto):
    #clase especializada de Contacto que permite incluir relacion
    def __init__(self,nombre,email,relacion):
        super().__init__(nombre,email)
        self.relacion=relacion


contactos_list=ContactList() #pasa a ser una lista vacia con nuevo metodo
contactos_list.append(Familiar(nombre="Daniela Gomez",email="daniela@gomez.cl",relacion="Madre")) #agrega objeto a lista
contactos_list.append(Contacto(nombre="Daniela Vega",email="daniela@vega.cl"))
print(list)
print(type(contactos_list))
print(contactos_list) #genera lista con objetos
contactos_list.append(Familiar(nombre="Juan Gomez",email="juan@gomez.cl",relacion="primo"))
contactos_list.append(Contacto(nombre="Natalia Lafourcade",email="natalia@lafourcade.cl"))
print(contactos_list) #genera lista con objetos

personas_llamadas_daniela=[]
print(contactos_list.buscar("Daniela"))
for contacto in contactos_list.buscar("Daniela"): #dentro de la lista de objetos, sublista que contiene el buscar
    print(contacto) #identifica objeto asociado
    print(contacto.nombre)
    personas_llamadas_daniela.append(contacto.nombre)
print(personas_llamadas_daniela)
