import amplpy
import pandas as pd
import matplotlib as plt

ampl = amplpy.AMPL(amplpy.Environment(r'C:\Users\diego\Documents\Diego_Aldunate\iPre\AMPL'))
ampl.read(r'C:\Users\diego\Documents\Diego_Aldunate\iPre\CS_2020_2\Modelo_AMPL\modelo_nl_costo.mod')
ampl.readData(r'C:\Users\diego\Documents\Diego_Aldunate\iPre\CS_2020_2\Modelo_AMPL\datos_precio_Fijo.dat')
ampl.setOption('solver','knitro')
#print(ampl.getOption('solver'))

ampl.solve()

fo=ampl.getObjective('FO')
#print(fo)
print("Valor de Funcion Objetivo es:" + str(fo.value()))


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




hold=ampl.getParameter('hold')
#print(hold.getValues()),print(type(hold.getValues()))
df_hold=pd.DataFrame(hold,columns={'a','Parte'})
#print(df.Parte)



########### Iteracion 2 ##################

#df_hold.Parte+=[0.02,0.0145,0.00875,0.0045]
#print(df_hold.Parte)

#valores=df_hold.Parte.tolist()
#print(valores)
#hold.setValues(valores)
#print(hold.getValues())

#ampl.solve()



#fo=ampl.getObjective('FO')
#print(fo)
#print("Valor de Funcion Objetivo es:" + str(fo.value()))


#hold.setValues([hold.getValues()+[0.02,0.0145,0.00875,0.0045]])
#print(hold.getValues())

'''
ap=ampl.getParameter('apren')
print(ap.getValues())
df_ap=pd.DataFrame(ap,columns={'Indice','Valor'})

por_ap=ampl.getParameter('por_ap')
print(por_ap.getValues())
df_por_ap=pd.DataFrame(por_ap,columns={'Indice','Valor'})
print(df_ap),print(df_por_ap)

por_ap=ampl.getParameter('por_ap').getValues().toPandas()
print(por_ap)
'''


amplpy.AMPL.close(ampl)