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
       return abs
    elif x==2:
       hom=ejercicio
       return hom
    elif x==3:
       esp=ejercicio
       retu
