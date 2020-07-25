######## paths #######
import os  #sistema operativo
path_relativo='data/archivo.txt' #desde carpeta que contiene archivo .py
#path = dir + base
with open(path_relativo,'rt') as archivo:
    lineas=archivo.readlines()
lineas

dirname1=os.path.dirname(path_relativo)
basename1=os.path.basename(path_relativo)
sin_extension,extension=os.path.splitext(basename1)

print(dirname1,basename1)
print(sin_extension,extension)

ruta=os.path.join(dirname1,basename1) #diferencias entre sistemas operativos

lista_de_contenidos=os.listdir("data")
print(lista_de_contenidos)
lista_de_contenidos=os.listdir(os.path.join("data","gato"))
print(lista_de_contenidos)

for raiz,directorios,archivos in os.walk("data",topdown=True):
    print("Raiz:",raiz)
    print("Archivos:")
    for archivo in archivos:
        print(os.path.join(raiz,archivo))
        #print(archivo,archivos) archivos=lista de archivos (definidos por funcion walk)
    print()
    for directorio in directorios:
        print(os.path.join(raiz,directorio))
        #print(directorio,directorios) #directorios=lista de directosios (definidos por funcion walk)

ruta_juego=os.path.join("data","gato","juego_1.txt")
with open(ruta_juego,'rt') as archivo:
    lineas=archivo.readlines()
print(lineas)
tablero=[]
for linea in lineas:
    fila=linea.strip().split(',') #strip linebreak, split separa caracteres segun deseado
    print(fila)
    tablero.append(fila)
#print(tablero)
tablero[2][2]='O'
for fila in tablero:
    print(fila)

ruta_juego_2=os.path.join("data","gato","juego_2.txt")
with open(ruta_juego_2,'wt') as archivo:
    for fila in tablero:
        fila_en_txt=",".join(fila)+"\n" #join=concatenar string previo con ","
        print(fila_en_txt)
        archivo.write(fila_en_txt)