import matplotlib.pyplot as plt
import numpy as np

def funcion_objetivo(funcion,rango):
    print(funcion)
    tiempo=[]
    valores=[]
    for iteracion in range(len(funcion)):
        print(funcion[iteracion])
        aux1,aux2=funcion[iteracion]
        tiempo.append(aux2)
        valores.append(aux1)
    plt.title('Funcion Objetivo')
    plt.plot(tiempo,valores)
    plt.axis([0, rango, 285922666, 300000000])  # genera largo de ejes
    plt.show()

def funcion_objetivo_hold(funcion,df,rango):
    valores = []
    tiempo=[]
    for iteracion in range(len(funcion)):
        aux1, aux2 = funcion[iteracion]
        valores.append(aux1)
        tiempo.append(aux2)
    for index,row in df.iterrows():
        lista=row.values.tolist()
        if index=='Cuarto':
            Cuarto=lista
        elif index=='Entero':
            Entero=lista
        elif index=='Medio':
            Medio=lista
        elif index=='Octavo':
            Octavo=lista

    plt.figure(1)
    plt.title('Funcion Objetivo - Costo de Inventario')
    plt.plot(Cuarto, valores, label='Cuarto')
    plt.plot(Entero, valores, label='Entero')
    plt.plot(Medio, valores, label='Medio')
    plt.plot(Octavo, valores, label='Octavo')
    plt.axis([0, 8, 287000000, 290000000])  # genera largo de ejes
    plt.legend(loc="center left",bbox_to_anchor=(1, 0.5))  # se genera un key de manera de identificar cada simulacion segun color
    plt.tight_layout()  # se ajusta legend al ancho de la pantalla

    plt.figure(2)
    plt.title('Costo de Inventario')
    plt.plot(tiempo,Cuarto, label='Cuarto')
    plt.plot(tiempo,Entero, label='Entero')
    plt.plot(tiempo,Medio, label='Medio')
    plt.plot(tiempo,Octavo, label='Octavo')
    plt.axis([0, rango, 0, 8])  # genera largo de ejes
    plt.legend(loc="center left",bbox_to_anchor=(1, 0.5))  # se genera un key de manera de identificar cada simulacion segun color
    plt.tight_layout()  # se ajusta legend al ancho de la pantalla

    plt.show()
    #if int(input('Desea Graficar 3D:\n[1] Si \n[2]  No\n'))==1:
    #    Graficar_3D(tiempo,[Cuarto,Entero,Medio,Octavo],valores)

def Graficar_3D(tiempo,lista,valores):
    fig=plt.figure()
    ax=plt.axes(projection="3d")
    ax.scatter3D(tiempo,lista[0],valores,cmap='hsv')
    ax.scatter3D(tiempo,lista[1],valores,cmap='hsv')
    ax.scatter3D(tiempo,lista[2],valores,cmap='hsv')
    ax.scatter3D(tiempo,lista[3],valores,cmap='hsv')
    plt.show()

def produccion(cuarto,entero,medio,octavo,cuarto_t,entero_t,medio_t,octavo_t,rango):
    #### Cuarto
    plt.figure(1)
    T = np.arange(0, rango+1 ,1)
    for iteracion in cuarto:
        plt.plot(T,iteracion)
    plt.title('Cantidad producida segun corte (Cuarto) por periodo')
    plt.axis([0,rango,7500,16000])


    plt.figure(2)
    T = np.arange(0, len(cuarto_t[0]), 1)
    for iteracion in cuarto_t:
        print(iteracion)
        plt.plot(T,iteracion)
    plt.title('Cantidad producida segun corte (Cuarto) por periodo')
    plt.axis([0,30,7500,16000])
    plt.show()

    #### Entero
    plt.figure(1)
    T = np.arange(0, rango + 1, 1)
    for iteracion in entero:
        plt.plot(T, iteracion)
    plt.title('Cantidad producida segun corte (Entero) por periodo')
    plt.axis([0, rango, 0, 7500])

    plt.figure(2)
    T = np.arange(0, len(entero_t[0]), 1)
    for iteracion in entero_t:
        print(iteracion)
        plt.plot(T, iteracion)
    plt.title('Cantidad producida segun corte (Entero) por periodo')
    plt.axis([0, 30, 0, 7500])
    plt.show()

    #Medio
    plt.figure(1)
    T = np.arange(0, rango + 1, 1)
    for iteracion in medio:
        plt.plot(T, iteracion)
    plt.title('Cantidad producida segun corte (Medio) por periodo')
    plt.axis([0, rango, 0, 6000])

    plt.figure(2)
    T = np.arange(0, len(medio_t[0]), 1)
    for iteracion in medio_t:
        print(iteracion)
        plt.plot(T, iteracion)
    plt.title('Cantidad producida segun corte (Medio) por periodo')
    plt.axis([0, 30, 0, 6000])
    plt.show()

    plt.figure(1)
    T = np.arange(0, rango + 1, 1)
    for iteracion in octavo:
        plt.plot(T, iteracion)
    plt.title('Cantidad producida segun corte (Octavo) por periodo')
    plt.axis([0, rango, 10000, 25000])

    plt.figure(2)
    T = np.arange(0, len(octavo_t[0]), 1)
    for iteracion in octavo_t:
        print(iteracion)
        plt.plot(T, iteracion)
    plt.title('Cantidad producida segun corte (Octavo) por periodo')
    plt.axis([0, 30, 10000, 25000])
    plt.show()
