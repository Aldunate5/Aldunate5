import practica
import os
#import Double_Down

def juego ():
    print("Bienvenido")
    print("Que desea jugar?")
    print("1. Modo chupar poto")
    print("2. Modo Focker")
    print("3. Practica")
    print("4. Puntaje")
    print("5. Salir")
    game=int(input())
    if game==1:
        print("en proceso")
    elif game==2:
        print("en proceso")
    elif game==3:
        practica.greetings()
    elif game==4:
        print("en proceso")
    elif game==5:
        os._exit(0)
    else:
        print("Tonto")
        juego()

juego()
print("chalupa")



