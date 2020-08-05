filename<-"murders.csv"
dir<-system.file("extdata",package = "dslabs")
fullpath<-file.path(dir,filename)
file.copy(fullpath,"murders.csv") #busca base murders y lo pega para luego importarlo

library(tidyverse)
dat<-read_csv(filename)


dir<-system.file(package = "dslabs")
list.files(path=dir) #entrega carpetas contenidas
filename %in% list.files(file.path(dir,"extdata")) #carpeta contiene archivo de interes
dir<-system.file("extdata", package = "dslabs") #genera subdirectorio
# fullpath combina directorios
# file.copy archivo a copiar, como se llamara en nuevo directorio

wd<-getwd() #working directory
list.files() #archivos wd
setwd("C:/Users/diego/Documents/Diego_Aldunate/R")
new_wd<-file.path(wd,"Diego_Aldunate\R")
getwd()

read_lines("murders.csv",n_max = 3)
dat<-read_csv(filename) 
class(dat) #class as tupple

#path<-system.file("extdata",package = "dslabs")
#files<-list.files(path)
#files
#archivo<-"olive.csv"
#fullpath<-file.path(files,archivo)
#file.copy(fullpath,"olive.csv")
#dat2<-read.csv("olive.csv")
#help("read_csv")
#names(dat2)

url <- "https://raw.githubusercontent.com/rafalab/dslabs/master/inst/extdata/murders.csv"
dat3<-read_csv(url)
download.file(url,"murders.csv") #it overrides 

#difference between read.csv and read_csv
#. -> as factor (or character i stringsAsFactors = FALSE); _ as tupple

path<-system.file("extdata",package = "dslabs")
filename<-"murders.csv"
fullpath1<-file.path(path,filename)
filename2<-"olive.csv"
fullpath2<-file.path(path,filename2)

file.path(path,filename)
x<-scan(file.path(path,filename),sep = ",", what = "c") #read cell by cell. Separa en coma y luego como character
x[1:10]
file.copy(fullpath2,"olive.csv")
getwd()        
files
