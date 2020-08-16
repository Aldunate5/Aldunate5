import random
import numpy
import matplotlib.pyplot as plt

np=10 #numero de simulaciones
ns=1000 #numero de instancias, 1000 => 10s
positions=numpy.zeros(np) #inicio en 0
HEAD=1;TAIL=2 #probabilidad de subir o bajar iguales (moneda)

for p in range(np):
    aux = [] #lista auxiliar que junta datos del eje y para cada simulacion
    x_axis=list(range(0,ns)) #eje x fijo para cada simulacion
    for step in range(ns):
        prob=random.randint(1,2)
        aux.append(positions[p])
        if prob==HEAD:
            positions[p]+=0.01 #salto hacia arriba de un 0.1m
        else:
            positions[p]-=0.01 #salto hacia abajo de un 0.1m
    plt.plot(x_axis,aux,label='Simulacion N' + str(p+1)) #para cada simulacion se agrega un label que lo identifique
                                                         # se agrega al grafico general
plt.axis([0,1000,-1,1]) #genera largo de ejes
plt.title("Random Walks", loc='center') #se genera titulo y se hace un label
plt.xlabel("Tiempo Transcurrido (10ms)");plt.ylabel("Distancia Recorrida (m)") #se generan ejes y se hace un label
plt.legend(loc="center left",bbox_to_anchor=(1,0.5)) #se genera un key de manera de identificar cada simulacion segun color
plt.tight_layout() #se ajusta legend al ancho de la pantalla
plt.show()