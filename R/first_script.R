a<-1
b<-1
c<--1

ls() #see objects

sol1<-(-b+sqrt(b^2-4*a*c))/(2*a)
sol2<-(-b-sqrt(b^2-4*a*c))/(2*a)

z<-100
x<-seq(1,z) #generate sequence
sum(x)

args(seq) #argumetnso de funciones


library(dslabs) 

data(murders)
class(murders) #define el tipo

str(murders) # info de cada columna
head(murders) #resumen de tabla
args(head)

murders

murders$state #$ aisla informacion de columna

install.packages("tidyverse")

estado<-murders$state
length(estado)
class(estado)
class(murders$region) #factor: subgrupo de division
levels(murders$region) #niveles de factores

region<-murders$region
value<-murders$population
region<-reorder(region,value, FUN = sum) #nuevo orden segun numero, como sacar el numero total?
levels(region)

record

mat<-matrix(1:12,4,3)
mat
mat[1:2,2:3] #eleccionar elementos especificos de una matriz
#[] para seleccionar elementos de matriz
as.data.frame(mat)

data(murders)
murders[1,4]
