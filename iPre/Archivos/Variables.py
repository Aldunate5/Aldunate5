def prod(df):
    for hold,new_df in df.groupby(level=0):
        if hold=='Cuarto':
            new_df.index=new_df.index.droplevel('hold')
            Cuarto=new_df.values.tolist()
            Cuarto_t=new_df.T.values.tolist()
        elif hold=='Entero':
            new_df.index=new_df.index.droplevel('hold')
            #new_df = new_df.T
            Entero=new_df.values.tolist()
            Entero_t = new_df.T.values.tolist()
        elif hold=='Medio':
            new_df.index=new_df.index.droplevel('hold')
            #new_df = new_df.T
            Medio=new_df.values.tolist()
            Medio_t = new_df.T.values.tolist()
        elif hold=='Octavo':
            new_df.index=new_df.index.droplevel('hold')
            #new_df = new_df.T
            Octavo=new_df.values.tolist()
            Octavo_t = new_df.T.values.tolist()
    return Cuarto,Entero,Medio,Octavo,Cuarto_t,Entero_t,Medio_t,Octavo_t

def inv():
    inventario = ampl.getVariable('W') #F,T,t=T
def inv_in():
    inventario_inicial=ampl.getVariable('W_0')
def perd():
    perdida=ampl.getVariable('L')
def cant_corte():
    cantidad_cort_corte=ampl.getVariable('X')
def cost_corte():
    costo_corte=ampl.getVariable('C_Corte')
def cost_inv():
    costo_inventario=ampl.getVariable('c_hold')
def price():
    precio=ampl.getVariable('preci')
def t_inv():
    tiempo_inv=ampl.getVariable('TInv')

"""
produccion=ampl.getVariable('P') #indice k y t
print(produccion.getValues())

produccion=ampl.var['P'].getValues()
print(produccion)
prod=list(produccion.getColumn('P.val'))
print(prod)

produccion=ampl.var['P'].getValues().toPandas()
produccion.index = pd.MultiIndex.from_tuples(produccion.index)
print(produccion)
produccion.index.names = ['Hold', 'Indice']
produccion.reset_index(inplace=True,level='Hold'),produccion.reset_index(inplace=True,level='Indice')
produccion=produccion.astype({'Indice':int})

print(produccion)
print(produccion.size)

#print(type(produccion['Indice'][0]))

cortes=[]
for index,row in produccion.iterrows():
    cortes.append(row['Hold'])
cortes=list(set(cortes))
print(cortes)

valores=[]
for tipo in cortes:
    valores_cortes=[]
    for index,row in produccion.iterrows():
        if row['Hold']==tipo:
            valores_cortes.append(row['P.val'])
    valores.append(valores_cortes)

print(valores)


print(produccion[produccion.Hold=='Cuarto'])
"""

#produccion.columns=['Tupla','P.val']
#print(produccion)
#produccion[['Hold', 'Iteracion']] = pd.DataFrame(produccion[''].tolist(), index=produccion.index)
