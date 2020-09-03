def prod():
    produccion = ampl.getVariable('P')  # indice k y t
def inv():
    inventario = ampl.getVariable('W')
def inv_in():
    inventario_inicial=ampl.getVariable('W_0')
def perd()
    perdida=ampl.getVariable('L')
def cant_corte():
    cantidad_cort_corte=ampl.getVariable('X')
def cost_corte()
    costo_corte=ampl.getVariable('C_Corte')
def cost_inv():
    costo_inventario=ampl.getVariable('c_hold')
def price():
    precio=ampl.getVariable('preci')
def t_inv():
    tiempo_inv=ampl.getVariable('TInv')


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


#produccion.columns=['Tupla','P.val']
#print(produccion)
#produccion[['Hold', 'Iteracion']] = pd.DataFrame(produccion[''].tolist(), index=produccion.index)
