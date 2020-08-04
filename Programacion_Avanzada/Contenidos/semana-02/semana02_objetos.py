#clase (define ambos) -> instancias
#atributos (datos, caracteristicas)
#metodos (acciones)

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

    def vender(self,nuevo_dueño):
        self.dueño=nuevo_dueño

    def leer_odometro(self):
        return self.__kilometraje

    def modificar_ubicacion(self):
        print("Calcular nueva ubicacion:")
        self._ubicacion=(self._ubicacion[0]+0.01,self._ubicacion[1]-0.01)

a=Auto("Kia","Sportage",2000,"Blanco",134000)
b=Auto("Suzuki","Grand Nomade",2015,"Naranjo",35695)

b.conducir(1450)
a.vender("Enrique")
print(b.leer_odometro())

class Departamento:
    def __init__(self,id,mts2,valor,num_dorms,num_banos):
        self.id=id
        self.mts2=mts2
        self.valor=valor
        self.num_dorms=num_dorms
        self.num_banos=num_banos
        self.vendido=False

    def vender(self):
        if not self.vendido:
            self.vendido=True
        else:
            print(f'Departamento {self.id} ya se vendio')

depto=Departamento(id=1,mts2=100,valor=5000, num_dorms=3, num_banos=2)
print(f'Vendido? {depto.vendido}')
depto.vender()
print(f'Vendido? {depto.vendido}')

#encapsulamiento: ocultar ciertos atributos de manera de modificarlos solo internamente en una clase
# convencion: _atributo o _metodo cuando es de uso interno

class Televisor:
    def __init__(self,pulgadas,marca):
        self.pulgadas=pulgadas
        self.marca=marca
        self.encendido=False #los que no se definen, tienen un valor predeterminado
        self.canal_actual=0
        self._clave="tv123"
    def encender(self):
        self.encendido=True
    def apagar(self):
        self.encendido=False
    def cambiar_canal(self,nuevo_canal): #se agrega nuevo valor externo a los que se definio previamente
        self._codificar_imagen()
        self.canal_actual=nuevo_canal
    def _codificar_imagen(self):
        print("Estoy convirtiendo una senal electrica en la imagen que estas viendo")

tv1=Televisor(17,"Sony")
tv2=Televisor(21,"Samsung")

tv1.cambiar_canal(2) #nuevo valor externo a los previamente definidos
print(tv1.canal_actual)



#en python todos son publicos (obtenibles en el codigo)
#mangling: doble underscore __ al inicio "oculta" (hace mas tedioso encontrarlo)
