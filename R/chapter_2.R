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

##############vectors#################
codes <- c(a,b,c)
country<- c("italia"=a, "chile"=b, "latvia"=c)
country
names(country)<-codes

args(seq)
seq(1,10,0.5)

country[c(1,3)]
class(country)

x<-c(180,"pais",230) #coerced: asume elementos de vector del mismo tipo
class(x)

x<-1:10
y<-as.character(x) #convertir tipo
as.numeric(y)

x<-c("1","b","3")
y<-as.numeric(x) #se generan NA

################ sort ##################
x<-c(31,4,89,10,5)
sort(x) #arma secuencia en orden
index<-order(x) #numera elementos en orden de la secuencia
rank(x)
#rank ordena segun seq original
#order ordena segun sort

murders$state
index<-order(murders$total)
murders$abb[index][1:5] #ordeno acorde a indice

max(murders$total) #equivalente para min
which.max(murders$total) #numera elemento max

#################vector operation###############3
vector<-c(23,5,7,30,29)
vector*3
vector-30

rate<-murders$total/murders$population*10^5
murders$state[order(rate)][1:5]
ind<-rate<0.71
sum(ind)
murders$state[ind]

west<-murders$region=="West"
safe<-rate<1
ind<-west & safe
murders$state[ind]

ind<-which(murders$state=="California")
rate[ind]

ind<-match(c("California","Texas"),murders$state) #equivalente a which para vectores
rate[ind]

############## plots ##################3
x<-murders$population / 10^6
y<-murders$total
args(plot)
plot(x,y)

z<-with(murders,rate)
hist(z)

murders$rate<-with(murders,total/population*100000)
boxplot(region~rate,data=murders)

x<- matrix(1:120,12,10)
image(x)
