import os
import random


abs=[]
hom=[]
esp=[]
rutina=[]
lista=[]

############################
def base1():
    global lista
    lista=[]
    file=open("core.txt") ##directorio##
    aux=[]
    for line in file:
        line=line.split(",")
        line = [x.strip().split("\n") for x in line]
        aux.append(line) ####buscar como hacer espacios y tabs de forma mas eficiente
    file.close()
    print(aux)
    print(lista)
    for a in range (len(aux)):
        lista.append([])
        for b in range (len(aux[a])):
            for c in range (len(aux[a][b])):
                lista[a].append(aux[a][b][c])
    lista_ej(lista)
    
    
    
def base2():
    global lista
    lista=[]
    file=open("hombro.txt") ##directorio##
    aux=[]
    for line in file:
        line=line.split(",")
        line = [x.strip().split("\n") for x in line]
        aux.append(line) ####buscar como hacer espacios y tabs de forma mas eficiente
    file.close()
    generar_lista(aux)
    
def base3():
    global lista
    lista=[]
    file=open("espalda.txt") ##directorio##
    aux=[]
    for line in file:
        line=line.split(",")
        line = [x.strip().split("\n") for x in line]
        aux.append(line) ####buscar como hacer espacios y tabs de forma mas eficiente
    file.close()
    print(lista)
    generar_lista(aux)
############################

#def generar_lista(aux):    
#    for a in range (len(aux)):
#        lista.append([])
 #       for b in range (len(aux[a])):
  #          for c in range (len(aux[a][b])):
   #             lista[a].append(aux[a][b][c])
    #lista_ej(lista)



def lista_ej(lista): #divide por zona
    global abs,hom,esp
    aux=[]
    for i in range (len(lista)):    
        aux.append(lista[i][1])
        zonas=list(set(aux))    
    for j in range (len(zonas)):
        aux=[]
        for i in range (len(lista)):
            if zonas[j]==lista[i][1]:
                aux.append(lista[i][0])
        abs.append(aux)
        hom.append(aux)
        esp.append(aux)
            
    
def generar_lista(x,count,lista):
    i=0
    while i<count:
        lista_corta(x,count,lista[i])
        i+=1
    if len(rutina)<x:
        while len(rutina)<x:
            value=random.randint(0,count)
            new=random.choice(lista[value])
            rutina.append(new)
            if rutina.count(new)>1:
                rutina.remove(new)
    return rutina
    
def lista_corta(x,count,lista):
    random.shuffle(lista)
    a=int(x/count)
    if x%count!=0:
        for i in range (a):
            rutina.append(lista[i])
    else:
        for i in range (a):
            rutina.append(lista[i])    

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

def greetings():
    global rutina
    rutina=[]
    
    print("Que quiere hacer?")
    print("1. Abdominales")
    print("2. Hombros")
    print("3. Espalda")      
    print("4. Informacion")
    print("5. Salir:")
    
    greet=input()#separar, recursion
    count1=len(abs)
    count2=len(hom)
    count3=len(esp)
    
    if greet == 1:
        base1()
        x=int(input("Cantidad de ejercicios:"))
        generar_lista(x,count1,abs)
        rutina_orden=random.sample(rutina,len(rutina))
        for i in range(len(rutina_orden)):
            print(rutina_orden[i])
        listo()
        
    elif greet==2:
        base2()
        x=int(input("Cantidad de ejercicios:"))
        generar_lista(x,count2,hombro)
        rutina_orden=random.sample(rutina,len(rutina))
        for i in range(len(rutina_orden)):
            print(rutina_orden[i])
        listo()

        
    elif greet==3:
        base3()
        x=int(input("Cantidad de ejercicios:"))
        generar_lista(x,count3,espalda)
        rutina_orden=random.sample(rutina,len(rutina))
        for i in range(len(rutina_orden)):
            print(rutina_orden[i])
        listo()

        
    elif greet==4:
        print("en proceso")
        
    else:
        print("Adios")
        os._exit(0)
   
greetings()
