import amplpy
import pandas as pd
import Modificar_Parametros
import Generar_Dataframe
import Graficar


ampl = amplpy.AMPL(amplpy.Environment(r'C:\Program Files\AMPL'))
ampl.read(r'C:\Users\diego\Documents\Diego_Aldunate\iPre\CS_2020_2\Modelo_AMPL\modelo_nl_costo.mod')
ampl.readData(r'C:\Users\diego\Documents\Diego_Aldunate\iPre\CS_2020_2\Modelo_AMPL\datos_precio_Fijo.dat')
ampl.setOption('solver','knitro')
#print(ampl.getOption('solver'))

hold = ampl.getParameter('hold').getValues().toPandas()


Generar_Dataframe.Generar(hold)




funcion_objetivo=[]
ampl.solve()
fo = ampl.getObjective('FO').value()
funcion_objetivo.append((fo, 0))

for simulacion in range(1):
    print(simulacion)
    """
    Variables
    """

    """
    Parametros
    """
    #modificable = [0.02, 0, 0, 0]
    modificable=[0.02, 0.0145, 0.00875, 0.0045]
    hold2 = ampl.getParameter('hold').setValues(Modificar_Parametros.hold_corte(hold,modificable,simulacion))


    ampl.solve()
    ######### Funcion Objetivo ###############
    fo = ampl.getObjective('FO').value()
    funcion_objetivo.append((fo, simulacion+1))

inventario=ampl.getVariable('W').getValues().toPandas()
Generar_Dataframe.Generar(inventario)
Generar_Dataframe.Anexo_tiempo(inventario)

#print(funcion_objetivo)
#Graficar.funcion_objetivo(funcion_objetivo)
#Graficar.funcion_objetivo_hold(funcion_objetivo,Generar_Dataframe.Frame())




