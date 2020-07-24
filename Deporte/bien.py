import os
import random


abs=[]
hom=[]
esp=[]
rutina=[]
rutina_orden=[]
zonas=[]

###############################3
def base(x):
    global abs, hom, esp, zonas
    if x==1:
       abs=[]
       file=open("core.txt","r")
    elif x==2:
       hom=[]
       file=open("hombro.txt","r")
    elif x==3:
       esp=[]
       file=open("espalda.txt","r")

    ejercicio=[]
    aux=[]

    for line in file:
        line=line.strip('\n')
        line=line.split(',')
        aux.append(line)
    file.close()

    aux2=[]
    for i in range (len(aux)):
        aux2.append(aux[i][1]) #agrega la zona de cada ejercicio
        zonas=list(set(aux2)) #elimina duplicados y genera lista de zonas

    for j in range (len(zonas)): #lista por zonas
        aux2=[]
        for i in range (len(aux)): #cada zona es una lista
            if zonas[j]==aux[i][1]:
                aux2.append(aux[i][0])
        ejercicio.append(aux2)

    if x==1:
       abs=ejercicio
    elif x==2:
       hom=ejercicio
    elif x==3:
       esp=ejercicio
    return ejercicio
##################################
def generar_lista(x,lista):
    global rutina_orden
    rutina_orden=[]
    i=0
    count=len(lista)
    if count>x:
        while i < x:
            a=random.randint(0,count-1)
            new=random.choice(lista[a])
            rutina.append(new)
            if rutina.count(new)>1:
                rutina.remove(new)
            else:
                i+=1
    else:
        while i<count:
            lista_corta(x,count,lista[i])
            i+=1
        if len(rutina)<x:
            while len(rutina)<x:
                value=random.randint(0,count-1)
                new=random.choice(lista[value])
                rutina.append(new)
                if rutina.count(new)>1:
                    rutina.remove(new)
                else:
                    i+=1
    rutina_orden=random.sample(rutina,len(rutina))
    print_lista(rutina_orden)
    
def lista_corta(x,count,lista):
    random.shuffle(lista)
    a=int(x/count)
    if x%count!=0:
        for i in range (a):
            rutina.append(lista[i])
    else:
        for i in range (a):
            rutina.append(lista[i])

######################################
def print_lista(lista):
    i=0
    while i < len(lista):
        i+=1
        print(str(i)+". "+str(lista[i-1]))

######################################
def informacion(orden,info):
    if orden==1:
        lista=[]
        x=base(info)
        for i in range(len(x)):
            for j in range(len(x[i])):
                lista.append(x[i][j])
        print_lista(lista)        
        
    elif orden==2:
        print_lista(zonas)
    else:
        orden=int(input("Incorrecto, pruebe otra vez"))
        informacion(orden)
    
    
    
######################################
def greetings():
    global rutina, lista
    rutina=[]
    lista=[]

    
    print("Que quiere hacer?")
    print("1. Abdominales")
    print("2. Hombros")
    print("3. Espalda")      
    print("4. Informacion")
    print("5. Salir:")
    
    greet=int(input())#separar, recursion
    
    if greet == 1:
        base(greet)
        x=int(input("Cantidad de ejercicios:"))
        generar_lista(x,abs)
        listo()
        
    elif greet==2:
        base(greet)
        x=int(input("Cantidad de ejercicios:"))
        generar_lista(x,hom)
        listo()

        
    elif greet==3:
        base(greet)
        x=int(input("Cantidad de ejercicios:"))
        generar_lista(x,esp)
        rutina_orden=random.sample(rutina,len(rutina))            
        listo()

        
    elif greet==4:
        
        print("Que musculo necesita:")
        print("1. Abdominales")
        print("2. Hombros")
        print("3. Espalda")
        info=int(input())

        print("Ordenar por:")
        print("1. Ejercicio")
        print("2. Zona")
        orden=int(input())
        informacion(orden,info)
        listo()

        
    else:
        print("Adios")
        os._exit(0)

##############################
def listo():
    a=0
    while a<1:
        print("Estas listo?")
        print("1. Si")
        print("2. No")
        listo=int(input())
        if listo==1:
            a+=1
            x=greetings()
        else:
            print("Sigue!")
################################


greetings()
