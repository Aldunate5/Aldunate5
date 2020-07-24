import os,sys
#from abdominales import*

print(os.getcwd())
sys.path.append("C:\Users\Diego\Desktop\python") 


def greetings():
    print("Que quiere hacer?")
    print("1. Abdominales")
    print("2.Informacion")
    print("3.Agregar Ejercicio")
    print("4. Salir:")
    greet=input()#separar, recursion
    count=len(abs)
    if greet == 1:
        x=int(input("Cantidad de ejercicios:"))
        generar_lista(x,count,abs)
        rutina_orden=random.sample(rutina,len(rutina))
        for i in range(len(rutina_orden)):
            print(rutina_orden[i])
        listo()
    elif greet==2:
        print("En proceso")
    elif greet==3:
        print("En proceso")
        #agregar_ejercicio()
    elif greet==4:
        print("Adios")
        os._exit(0)
    else:
        print("incorrecto")
        greetings()
