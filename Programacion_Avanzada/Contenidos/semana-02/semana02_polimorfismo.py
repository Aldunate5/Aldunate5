#polimorfisimo: utilizar objetos de distinto tipo con la misma interfaz
#overriding: sobereescribir metodo existente en subclase
#overloading: metodo con mismo nombre, distinto argumentos y sus tipos

import statistics

class Variable:
    def __init__(self,data):
        self.data=data
    def representante(self):
        pass

class Ingresos (Variable):
    def representante(self):
        return statistics.mean(self.data)


class Comunas (Variable):
    def representante(self):
        return statistics.mode(self.data)

class Puestos (Variable):
    categorias=['Practicante','Analista','SubGerente','Gerente']
    def representante(self):
        puestos=[]
        for cargo in self.data:
            puestos.append(Puestos.categorias.index(cargo))
        maximo=max(puestos)
        return Puestos.categorias[maximo]

lista_pesos = Ingresos([50, 80, 90, 150, 45, 65, 78, 89, 59, 77, 90])
lista_comunas = Comunas(['Providencia', 'Macul' , 'La Reina' ,'Santiago', 'Providencia', 'Puente Alto',
                        'Macul', 'Santiago', 'Santiago'])
lista_puestos = Puestos(['SubGerente', 'Analista','SubGerente','Analista','Practicante',
                        'Practicante'])

#se invoca el mismo metodo sobre objetos de distinto tipo, y lo interpreta de acuerdo a su definicion

print(lista_pesos.representante())
print(lista_comunas.representante())
print(lista_puestos.representante())
#si no encuentra metodo, utiliza el de la clase superior

#overloading
#ej el + depende de si son strings, listas, etc.
a=[1,2,3]
b=[4,5,6]
c="Hola"
d="mundo"
print(a+b,c+d)
#mismo operador funciona de distinta manera de acuerdo al argumento

class Carro:
    def __init__(self,pan,leche,agua):
        self.pan=pan
        self.leche=leche
        self.agua=agua

    def __add__(self, other):
        suma_pan = self.pan + other.pan
        suma_leche = self.leche + other.leche
        suma_agua = self.agua + other.agua
        return Carro(suma_pan, suma_leche, suma_agua)

    def __str__(self): #metodo incluye como se veria el print
        return f"Pan:{self.pan}, Leche: {self.leche}, Agua: {self.agua}"

carro_1=Carro(1,2,3)
carro_2=Carro(3,4,5)
carro_sumado=carro_1+carro_2 #se utiliza metodo add, el que incluye las 3 variables en cuestion
print(carro_sumado)
# generalizable a los demas operadores


import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def magnitud(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __lt__(self, otro_punto):
        return self.magnitud < otro_punto.magnitud

v1 = Vector(2, 4)
v2 = Vector(8, 3)
print(v1 < v2)

class Fraccion:
    def __init__(self,numerador,denominador):
        self.numerador=numerador
        self.denominador=denominador
    def __repr__(self):
        return f"Fraccion:{self.numerador},{self.denominador}"

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

frac=Fraccion(3,4)
repr(frac) #repr: representacion para otro programador sin ambiguedades
str(frac) #str: leible por cualquier
print(frac) #default, es el objeto de la clase, se prioriza el str en el print, si no hay pasa al repr

#duck typing, clases distintas tienen mismos metodos. Uno se da cuenta de cual es cual al ejecutarlo