import amplpy
import pandas as pd
import Modificar_Parametros
import Generar_Dataframe
import Variables
import Graficar


ampl = amplpy.AMPL(amplpy.Environment(r'C:\Program Files\AMPL'))
#ampl = amplpy.AMPL(amplpy.Environment(r'C:\Users\diego\Documents\Diego_Aldunate\iPre\AMPL'))
ampl.read(r'C:\Users\diego\Documents\Diego_Aldunate\iPre\CS_2020_2\Modelo_AMPL\modelo_nl_costo.mod')
ampl.readData(r'C:\Users\diego\Documents\Diego_Aldunate\iPre\CS_2020_2\Modelo_AMPL\datos_precio_Fijo.dat')
ampl.setOption('solver','knitro')
#print(ampl.getOption('solver'))

#### Definir Parametros ###
hold = ampl.getParameter('hold').getValues().toPandas()
hold_df=Generar_Dataframe.Generar(hold)

alpha = ampl.getParameter('alfa').getValues().toPandas()
alpha_df=Generar_Dataframe.Generar(alpha)

beta = ampl.getParameter('beta').getValues().toPandas()
beta_df=Generar_Dataframe.Generar(beta)

# Iteracion 0#
funcion_objetivo=[]
ampl.solve()

### Definir Variables ###
produccion = ampl.getVariable('P').getValues().toPandas()
produccion_df=Generar_Dataframe.Generar(produccion)

inventario = ampl.getVariable('W').getValues().toPandas()
inventario_df=Generar_Dataframe.Generar(inventario)
print(inventario_df)

fo = ampl.getObjective('FO').value()
funcion_objetivo.append((fo, 0))

rango=100
for simulacion in range(rango):
    print(simulacion)

    ################################# Parametros ###############################

    ############### Hold ######################
    modificable_hold=[0.02, 0.0145, 0.00875, 0.0045]
    valores_modificados_hold=Modificar_Parametros.hold_corte(hold,modificable_hold).tolist()

    hold_df=Generar_Dataframe.Anexar(valores_modificados_hold,simulacion,hold_df)
    #print(hold_df)
    ampl.getParameter('hold').setValues(valores_modificados_hold)

    ############### Alpha ######################
    '''
    modificable_alpha = [6.4, 3.2, 1.6, 0.8]
    valores_modificados_alpha = Modificar_Parametros.max_demanda(alpha, modificable_alpha).tolist()

    alpha_df = Generar_Dataframe.Anexar(valores_modificados_alpha, simulacion, alpha_df)
    print(alpha_df)
    ampl.getParameter('alfa').setValues(valores_modificados_alpha)

    ############### Beta ######################
    modificable_beta = [0.00072, 0.000168, 0.0000208, 0.00000712]
    valores_modificados_beta = Modificar_Parametros.tasa_demanda(beta, modificable_beta).tolist()

    beta_df = Generar_Dataframe.Anexar(valores_modificados_beta, simulacion, beta_df)
    print(beta_df)
    ampl.getParameter('beta').setValues(valores_modificados_beta)
    '''

    ################################ Solve #####################################
    ampl.solve()

    ############################# Variables ############################

    produccion = ampl.getVariable('P').getValues().toPandas()
    produccion_df=Generar_Dataframe.Anexo_tiempo(produccion['P.val'],simulacion,produccion_df)
    Generar_Dataframe.Indexar(produccion_df,'produccion')


    inventario = ampl.getVariable('W').getValues().toPandas()
    inventario_df=Generar_Dataframe.Anexo_tiempo_tiempo(inventario['W.val'],simulacion,inventario_df)
    Generar_Dataframe.Indexar(inventario_df,'inventario')



    ############################ Funcion Objetivo #######################
    fo = ampl.getObjective('FO').value()
    funcion_objetivo.append((fo, simulacion+1))


#print(funcion_objetivo)
#print(hold_df)
#print(produccion_df,inventario_df)
Prod_Cuarto,Prod_Entero,Prod_Medio,Prod_Octavo,Prod_Cuarto_t,Prod_Entero_t,Prod_Medio_t,Prod_Octavo_t=Variables.prod(produccion_df)
#Graficar.funcion_objetivo(funcion_objetivo,rango)
#Graficar.funcion_objetivo_hold(funcion_objetivo,hold_df,rango)
#print(Prod_Cuarto)
Graficar.produccion(Prod_Cuarto,Prod_Entero,Prod_Medio,Prod_Octavo,Prod_Cuarto_t,Prod_Entero_t,Prod_Medio_t,Prod_Octavo_t,rango)



