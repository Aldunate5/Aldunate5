import pandas as pd


def Generar (parametro):
    df=parametro.copy()
    return df

def Anexar(columna,numero,df):
    df.insert(loc=(numero+1),column=str(numero+1),value=columna)
    return df

def Anexo_tiempo(columna,numero,df):
    df.insert(loc=(numero+1),column='Iteracion' + str(numero+1),value=columna)
    return df

def Anexo_tiempo_tiempo(columna,numero,df):
    df.insert(loc=(numero+1),column='Iteracion' + str(numero+1),value=columna)
    return df

def Indexar(df,nombre):
    df.index = pd.MultiIndex.from_tuples(df.index)
    if nombre=='produccion':
        df.index.names = ['hold', 'tiempo']
    elif nombre=='inventario':
        df.index.names=['hold','tiempo','tiempo']

def Frame():
    return df