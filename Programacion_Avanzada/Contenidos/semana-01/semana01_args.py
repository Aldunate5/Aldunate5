#parametros: nombres que recibe funcion; argumentos: valores efectivos

def ejemplo(a,b,c):
    print(f'a:{a},b:{b},c:{c}')
#se pueden definir argumentos por default; regla no definir sin defecto despues de con defecto


ej1=ejemplo("hola","mundo",42)
ej2=ejemplo(b="mundo",c=42,a="hola")
ej1,ej2
#predeterminado es por orden de argumento; o asociar nombre de llave con su valor (keyword argument)
#reglas: no usar posicional despues de palabra clave y no repetir palabra clave de posicional

lista=['hola','mundo',42]
tupla=('hola','mundo',42)
diccionario={'a':'hola','b':'mundo','c':42}

#deben calzar dimensiones
ejemplo(*lista)
ejemplo(*tupla)
ejemplo(**diccionario)

def func1 (*args):
    print(f'func1:{args}')

def func2 (**kwargs):
    print(f'func1:{kwargs}')

#*args permite definir cantidad arbitraria de arg posicionales;
#**kwargs permite definir cantidad arbitraria de arg por palabra clave

def func3 (a,b=3, *args, **kwargs): #nombres args y kwargs pueden variar
    print(f'a:{a},b:{b},args:{args},kwargs:{kwargs}')

func3(1,2,"3",c=5,d="7") #se rellena orden, luego los restantes se separan segun naturaleza
