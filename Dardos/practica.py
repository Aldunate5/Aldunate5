import random


def modo(aux, x, y, tipo):
    if aux == 1:
        if x == 21:
            tipo.remove(tipo[len(tipo) - 1])
            y = random.choice(tipo)
            print(x, y)
            listo()
        elif x < 21:
            print(x, y)
            listo()

    elif aux == 2:
        print(x)
        listo()

    elif aux == 3:
        tipo = ["doble", "triple"]  # arreglar
        y = random.choice(tipo)
        print(y)
        listo()

    elif aux == 4:
        print("Adios")

    else:
        print("incorrecto")
        greetings()


def listo():
    a = 0
    input()
    while a < 1:
        print("Quieres seguir")
        print("1. Si")
        print("2. No")
        listo = int(input())
        if listo == 1:
            a += 1
            x = greetings()
        else:
            a += 1
            print("Adios")


def greetings():
    print("Bienvenido")
    print("1. Random")
    print("2. Modalidad")
    print("3. Salir:")
    greet = int(input())  # separar, recursion

    x = random.randint(1, 21)
    tipo = ["simple", "doble", "triple"]
    y = random.choice(tipo)

    if greet == 1:
        aux = random.randint(1, 3)
        modo(aux, x, y, tipo)
        listo()


    elif greet == 2:
        print("1. Combinacion")
        print("2. Numero")
        print("3. Doble o Triple")
        print("4. Salir:")
        aux = int(input("Que modalidad desea jugar \n"))
        if aux==4:
            print("Adios")
        else:
            modo(aux, x, y, tipo)
            listo()

    elif greet == 3:
        print("Adios")
        #salir modo practica