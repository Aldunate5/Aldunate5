library(dslabs)
data("murders")
murders_rate<-murders$total/murders$population*10^5
ind<-which.min(murders_rate)

if(murders_rate[ind]<0.25){
  print(murders$state[ind])
}else{
  print("No state present death rate that low")
}
a <- 0
ifelse(a>0,1/a,NA)
a<-c(0,1,2,-4,5)
result<-ifelse(a>0,1/a,NA)

data("na_example")
no_nas<- ifelse(is.na(na_example),0,na_example)
sum(is.na(no_nas))

z<-c(TRUE,TRUE,FALSE)
any(z) #True if any entry is True
all(z) #True if all are True

########### functions ##############
avg<-function(x){ #variables dentro de funciones no se guardan en workspaces
  s<-sum(x)
  n<-length(x)
  s/n #entrega valor a retornar
}
x<-1:100
avg(x)
identical(mean(x),avg(x))

######### Namespaces ####### funciones dentro de distintos packages cumplen distintas funciones con mismo nombre
search() #orden de prioridad
#stats::filter();dplyr::filter 
#se menciona el package, y luego la funcion que pertenece

compute_s_n<-function(n){
  x<-1:n
  sum(x)
}
a=compute_s_n(25)
m<-25
s_n=vector(length=m) #empty vector largo m
for (n in 1:m){
  s_n[n]<-compute_s_n(n)
}
print(s_n)
n<-1:m
plot(n,s_n)

####### vectorization ##########
x<-1:10
y<-1:10
sqrt(x) #aplica funcion a cada elemento de vector
x*y

sapply(x, sqrt) #aplica funcion a cada elemento de un tipo de informacion
z<-matrix(1:12,3,4)
z1<-lapply(z,sqrt) #sapply,apply, etc..
print(z1)
