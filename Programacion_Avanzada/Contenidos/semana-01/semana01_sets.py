#tiempo revisar elemento en set es constante

lista_artistas=["ONJ","DY","Sting","DT","ML","Sting"]
set(lista_artistas)
print(set(lista_artistas)) #no repite elementos
conjunto_artistas={"ONJ","DY","Sting","DT","ML","Sting"} #forma de generar set
print(conjunto_artistas)

conj_heterogeneo={"cero",3,5,"cuatro"} #conjunto heterogeneo

#sets por comprension

from collections import namedtuple

Pelicula = namedtuple("Pelicula",["titulo","director","genero"])
peliculas = [Pelicula("Into the Woods","Rob Marshall","Aventura"),
             Pelicula("American Sniper","Clint Eastwood","Accion"),
             Pelicula("Taken","Pierre Morel","Accion")]

directores_accion={p.director for p in peliculas if p.genero=="Accion"}
print(directores_accion)

#sets no se identan directores_accion[0]
len(conjunto_artistas)
conjunto_artistas.add("Taylor Swift")
print(conjunto_artistas)
conjunto_artistas.remove("ONJ") #error eliminar algo que no esta
print(conjunto_artistas)
conjunto_artistas.discard("The Beatles") #alternativa que no arroja error
print(conjunto_artistas)

#se puede iterar, pero al no estar identado se reduce el tiempo de busqueda
for artista in conjunto_artistas:
    print(f'Saluden a {artista}')
print("Sting" in conjunto_artistas)

#operacion de conjuntos
set_a={0,1,2,3}
set_b={5,4,3,2}

set_union=set_a.union(set_b) #alternativa |
set_interseccion=set_a & set_b #alternativa .intersection

set_difference_a_b = set_a - set_b #el orden si importa; alternativa .difference
set_difference_b_a = set_b - set_a

set_sym_dif=set_a ^ set_b #diferencia de ambos; alternativa .symmetric_difference

#>,<,= determinar superset, subset o igualdad

#pasar de un set a una lista y viceversa
lista=["A","B","A","D","X","X"]
set_lista=set(lista)
print(set_lista)
lista_set=list(set_lista)
print(lista_set)
lista_set.sort()
print(lista_set)