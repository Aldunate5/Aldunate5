#pass: operacion nula (donde se planea escribir despues)
class Video:
    pass

vid=Video()

#se agregan atributos nuevos
vid.ext='avi'
vid.size='1024'

print(vid.ext,vid.size)

class Imagen:
    def __init__(self):
        self.ext=''
        self.size=''
        self.data=''


img = Imagen ()
img.ext='bmp'
img.size='8'
img.data=[255,255,255,200,34,35]

#se agregan nuevos atributos a otros ya existentes
print(img) #muestra string de qe tipo de archivo es
print(img.ext,img.size,img.data)
img.ids = 20
print(img.ext,img.size,img.data,img.ids)
#no es una buena practica agregar atributos de manera externa

########### Tuplas #########
# #(ordenada e inmutable pero heterogeneas) - tipo de clase de python
# permite modificar por mismo tipo de elemento en tupla

a=tuple() #tupla vacia
b=(0,1,2) #utilizar parentesis
c=(0,)
d=0,'uno'
print(a)
print(b)
print(b[0],b[1])
print(c)
print(d[0],d[1])

a=(img,'es','una foto')
a[0].ext='gif'
print(a[0].ext,a[0].size,a[0].data,a[1],a[2])

def calcular_geometria(a,b):
    area=a*b
    perimter=(2*a)+(2*b)
    mpa=a/2
    mpb=b/2
    return (area,perimter,mpa,mpb) #parentesis entrega tupla

data=calcular_geometria(20.0,10.0)
print(f"1:{data}") #entrega el return de la funcion
print(type(data)) #parentesis entrega una tupla
p=data[1]
print(f"2:{p}")
a,p,mpa,mpb=data #se generan variables independientes desde la tupla
print(f"3:{a},{p},{mpa},{mpb}")
a,p,mpa,mpb=calcular_geometria(20.0,10.0) #se desempaquetan directamente
print(f"3:{a},{p},{mpa},{mpb}")

data=(400,20,1,4,10,11,12,500)
a=data[1:3]
print('1:{0}'.format(a))
a=data[3:]
print('2:{0}'.format(a))
a=data[:5]
print('3:{0}'.format(a))
a=data[2::2]
print('4:{0}'.format(a))
a=data[1:6:2]
print('5:{0}'.format(a))
a=data[::-1]
print('6:{0}'.format(a))

from collections import namedtuple  #alternativas a clases
Register = namedtuple('Register_type',['RUT','name','age'])

c1=Register('19246988-0','Diego',23)
c2=Register('23066987-2','Dante',5)

print(c1.RUT)
print(c2.RUT)
print(c2)
print(type(c2))

#c1.rut='Cristian'

######### Listas ###############

lista=list() #lista vacia lista =[]
lista.append((2015,3,4)) #agrego una tupla a lista
lista.append((2015,3,4)) #agrego otra tupla a la lista
print(lista,len(lista))

lista=[1,'string',20.5,(23,45)]
lista.append('ultimo')
print(lista)
print(lista[1])
print(len(lista))

lista.insert(1,'of Monsters and Men') #agrega en un numero especifico

#lista por compresion: genera lista utilizando como for de otra lista
#cantidad_letras=[len(elemento) for elemento in lista]
#print(cantidad_letras)

class Pieza:
    id_ =0
    def __init__(self,pieza):
        Pieza.id_ += 1
        self.id = Pieza.id_
        self.tipo=pieza


piezas=[]
piezas.append(Pieza('Alfil'))
piezas.append(Pieza('Peon'))
piezas.append(Pieza('Rey'))
piezas.append(Pieza('Reina'))

for pieza in piezas:
    print('id:{0} - tipo de pieza:{1}'.format(pieza.id,pieza.tipo))

