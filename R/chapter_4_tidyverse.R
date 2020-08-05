library(tidyverse)
library(dslabs)
library(dplyr)

murders<-mutate(murders, rate=total/population *10^5) #mutate adds column to data frame
murders

filter(murders, rate<=0.71) #subsetting from data frame

new_table<-select(murders,state,region,rate)
filter(new_table,rate<=0.71)

select(murders,state,population) %>% head()

filter(murders,state=="New York")
filter(murders,state!="Florida")

# %>% pipe, envia output de uno a otro

murders %>% select(state,region,rate) %>% filter(rate<=0.71)

16 %>% sqrt() %>% log2()

data("heights")
heights
s<-heights %>% filter(sex=="Male") %>%
  summarise(average=mean(height), s.d=sd(height)) #define new "table" as summary of information
s

heights %>% filter(sex=="Male") %>%
  summarise(median=median(height), minimum=min(height),maximum=max(height)) #only single value output

us_murder_rate <- murders%>% summarise(rate=sum(total)/sum(population)*10^5)
class(us_murder_rate)
us_murder_rate <- murders%>% summarise(rate=sum(total)/sum(population)*10^5) %>% pull(rate)
class(us_murder_rate)

heights%>% group_by(sex) %>% summarise(average=mean(height),standard_deviation=sd(height))

murders %>% arrange(population) %>% head() #arranges by "popuation", ascendente por default arrange(desc)
murders %>% arrange(region,rate) %>% head() #ordena en primer filtro y luego en segundo los subset

#ignore data not available na.rm=TRUE
# tibbles different from data frame -> used in group_by and summarise

rates<-filter(murders, region=="South") %>% mutate(rate=total/population*10^5) %>% .$rate
rates
filter(murders,region=="South")

#.$ genera un vector de los elementos del filtro

my_summary<-function(dat){
  x<-quantile(dat$height,c(0,0.5,1))
  tibble(min = x[1],med=x[2],max=x[3])
}
heights %>% group_by(sex) %>% do(my_summary(.))

compute_s_n <- function(n){
  x <- 1:n
  sum(x)
}
n <- 1:25
s_n <- sapply(n, compute_s_n)

library(purrr) 
#map: output as specific type of element
s_n<-map(n,compute_s_n) #list
class(s_n)
s_n<-map_dbl(n,compute_s_n) #number vector
class(s_n)
#s_n<-map_df(n,compute_s_n) #tibble
#in function sum(x) -> tibble(sum=sum(x))
#class(s_n)

#case_when -> condicional util para segmentar
murders %>% 
  mutate(group = case_when(
    abb %in% c("ME", "NH", "VT", "MA", "RI", "CT") ~ "New England",
    abb %in% c("WA", "OR", "CA") ~ "West Coast",
    region == "South" ~ "South",
    TRUE ~ "Other")) %>%
  group_by(group) %>%
  summarize(rate = sum(total) / sum(population) * 10^5) 

x<-5
a<-3
b<-7
between(x,a,b)
