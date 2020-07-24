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
    global set

    file = open("base.txt", "r")
    set = []
    next(file)
    for linea in file:
        linea=linea.replace("\n","")
        turno_aux=[]
        turno_aux.append(linea)
        set.append(turno_aux)

        jugador=0
        while jugador < (len(lista)-1):

            puntaje=int(input("Ingrese puntaje \n"))
            turno_aux.append(puntaje)
            jugador=jugador+1
        tabla=int(input("Desea Ver Tabla? \n [1] Si \n [2] No \n"))
        if tabla==1:
            tabla_puntaje()


def tabla_puntaje():
    global lista

    file_final = open("tabla.txt", "w+")
    for i in lista:
        file_final.write(i + " "*6)
    file_final.write("\n")
    for linea in set:
        for puntaje in linea:
            file_final.write(str(puntaje) + " "*6)
        file_final.write("\n")
    file_final.close()


def run():
    global file

    file = open("base.txt", "w+")
    jugadores()
    interfaz()
    turnos()
