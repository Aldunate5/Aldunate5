import pandas as pd


def Generar (parametro):
    global df
    df=parametro.copy()
    #print(df)

def Anexar(columna,numero):
    df.insert(loc=(numero+1),column=str(numero+1),value=columna)
    #print(df)

def Anexo_tiempo(columna,numero,tiempo):
    df.insert(loc=(numero+1),column='Tiempo',value=columna)
    df.insert(loc=(numero+2),column='Tiempo',value=columna)
    print(df)
def Frame():
    return df