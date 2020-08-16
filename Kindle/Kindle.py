import os

file=open("libros.txt","r")
lista=[]
lista_libros_autor=[]
autor=""

for linea in file:
    aux = file.readline()
    aux=aux.replace('\x00','')
    aux=aux.strip('\n')
    aux=aux.replace("|",'')

    if "+" in aux:
        autor=aux[4:]
        print(autor)
    if "+" not in aux:
        libro=aux[7:]
        lista_libros_autor.append(libro)

        lista_libros_autor.append(autor)
        lista_libros_autor
        lista.append(lista_libros_autor)
    lista_libros_autor=[]
print(lista)

file.close()

final=open("Lista_Final.txt","w")
for coleccion in lista:
    nueva_linea=f"{coleccion[0]},{coleccion[1]}"
    final.writelines(f"{nueva_linea} \n")
final.close()