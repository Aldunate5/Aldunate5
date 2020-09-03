import matplotlib.pyplot as plt

def funcion_objetivo(funcion):
    print(funcion)
    tiempo=[]
    valores=[]
    for iteracion in range(len(funcion)):
        print(funcion[iteracion])
        aux1,aux2=funcion[iteracion]
        tiempo.append(aux2)
        valores.append(aux1)
    plt.plot(tiempo,valores)
    plt.axis([0, 50, 285922666, 300000000])  # genera largo de ejes
    plt.show()

def funcion_objetivo_hold(funcion,df):

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
    plt.plot(Cuarto, valores, label='Cuarto')
    plt.plot(Entero, valores, label='Entero')
    plt.plot(Medio, valores, label='Medio')
    plt.plot(Octavo, valores, label='Octavo')
    plt.axis([0, 8, 287000000, 290000000])  # genera largo de ejes
    plt.legend(loc="center left",bbox_to_anchor=(1, 0.5))  # se genera un key de manera de identificar cada simulacion segun color
    plt.tight_layout()  # se ajusta legend al ancho de la pantalla

    plt.figure(2)
    plt.plot(tiempo,Cuarto, label='Cuarto')
    plt.plot(tiempo,Entero, label='Entero')
    plt.plot(tiempo,Medio, label='Medio')
    plt.plot(tiempo,Octavo, label='Octavo')
    plt.axis([0, 100, 0, 8])  # genera largo de ejes
    plt.legend(loc="center left",bbox_to_anchor=(1, 0.5))  # se genera un key de manera de identificar cada simulacion segun color
    plt.tight_layout()  # se ajusta legend al ancho de la pantalla

    plt.show()
    if int(input('Desea Graficar 3D:\n[1] Si \n[2]  No\n'))==1:
        Graficar_3D(tiempo,[Cuarto,Entero,Medio,Octavo],valores)

def Graficar_3D(tiempo,lista,valores):
    fig=plt.figure()
    ax=plt.axes(projection="3d")
    ax.scatter3D(tiempo,lista[0],valores,cmap='hsv')
    ax.scatter3D(tiempo,lista[1],valores,cmap='hsv')
    ax.scatter3D(tiempo,lista[2],valores,cmap='hsv')
    ax.scatter3D(tiempo,lista[3],valores,cmap='hsv')
    plt.show()