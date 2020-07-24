import random


def jugadores():
    global lista

    jugador=int(input("Inserte numero de jugadores \n"))
    lista=[" "]
    for i in range(jugador):
        aux=input("Nombre de Jugador \n")
        lista.append(aux)
    for i in lista:
        file.write(" "*6 + i)

def interfaz ():
    global lista_turnos
    lista_turnos=["15","16","Doble","17","18","Triple","19","20","Bull",]
    for i in range (len(lista_turnos)):
        file.write("\n" + lista_turnos[i])
    file.close()

def turnos ():
    file = open("base.txt", "r")
    set = []
    next(file)
    for linea in file:
        print(linea)
        linea=linea.replace("\n","")
        turno_aux=[]
        turno_aux.append(linea)
        print(turno_aux)
        set.append(turno_aux)
        print(set)

        jugador=0
        while jugador < (len(lista)-1):

            puntaje=int(input("Ingrese puntaje \n"))
           turno_aux.append(puntaje)
            jugador=jugador+1

def puntos():
    for i in lista:
        puntos_jugador=[]

file = open("base.txt", "w+")
jugadores()
interfaz()
turnos()
