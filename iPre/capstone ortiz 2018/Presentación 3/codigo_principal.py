from gurobipy import *
import numpy as np
"""Para cada día, tenemos que observar si la cantidad de insumos que se recibe
es mayor que el límite óptimo, intentando satisfacer la demanda
siempre."""

"""El siguiente modelo solo revisa hacia el futuro en 1 día:
Tenemos 2 escenarios:
a) Si la cantidad de insumos es mayor a 43, simplemente cortamos
b) Si la cantidad de insumos es menor a 43, vemos si se puede suplir la demanda
con el día anterior"""
###############################################################################
##DATOS DE LA DEMANDA Y PRECIO ÓPTIMO##
indices_patrones = [i for i in range(1,22)]
indices_piezas = [i for i in range(1,10)]
precios_optimos = {}
lista_precios = [66000, 50000, 107500, 35000, 37778, 235000, 38000, 48000, 18572]
for i in indices_piezas:
    precios_optimos[i] = lista_precios[i-1]

demanda_optima = {}
lista_demandas = [33, 35, 43, 21, 34, 47, 19, 24, 13]
for i in indices_piezas:
    demanda_optima[i] = lista_demandas[i-1]
###############################################################################
##COSTO PATRONES (considera la utilidad de mandar a astillar lo que sobra)##
costo_patron = {}
lista_costos_patrones = [132800, 141000, 83750, 109300, 81700, 81700, 85800, 89900, 160400, 138950,
138950, 105200, 83750, 109300, 141000, 141000, 105200, 91950, 179800, 162450, 91950]
for i in indices_patrones:
    costo_patron[i] = lista_costos_patrones[i-1]
###############################################################################
##PATRONES##
piezas_patron = {}
piezas_patron[1] = [2, 0, 0, 0, 2, 1, 1, 0, 0]
piezas_patron[2] = [0, 2, 1, 0, 0, 2, 1, 0, 0]
piezas_patron[3] = [0, 0, 1, 1, 0, 0, 0, 1, 1]
piezas_patron[4] = [1, 0, 0, 1, 0, 1, 1, 1, 0]
piezas_patron[5] = [0, 0, 0, 0, 1, 2, 0, 0, 1]
piezas_patron[6] = [0, 1, 0, 1, 0, 0, 0, 1, 1]
piezas_patron[7] = [0, 0, 1, 0, 1, 0, 0, 1, 1]
piezas_patron[8] = [0, 0, 0, 0, 0, 1, 1, 2, 0]
piezas_patron[9] = [3, 1, 1, 0, 0, 1, 1, 0, 0]
piezas_patron[10] = [0, 2, 1, 2, 0, 0, 0, 1, 0]
piezas_patron[11] = [1, 0, 0, 3, 0, 0, 2, 0, 0]
piezas_patron[12] = [0, 1, 0, 0, 3, 0, 0, 1, 0]
piezas_patron[13] = [0, 0, 0, 0, 1, 1, 1, 0, 1]
piezas_patron[14] = [0, 2, 0, 0, 2, 0, 0, 0, 1]
piezas_patron[15] = [1, 0, 0, 4, 0, 0, 0, 1, 0]
piezas_patron[16] = [0, 2, 1, 0, 0, 2, 1, 0, 0]
piezas_patron[17] = [0, 0, 3, 0, 0, 0, 1, 1, 0]
piezas_patron[18] = [0, 0, 0, 0, 0, 0, 3, 0, 1]
piezas_patron[19] = [5, 2, 0, 0, 0, 1, 0, 0, 0]
piezas_patron[20] = [1, 4, 0, 0, 1, 0, 1, 0, 0]
piezas_patron[21] = [0, 1, 0, 1, 0, 0, 0, 0, 2]
###############################################################################
##INFORMACIÓN DE ALFAS Y BETAS##
alfas=(66, 71, 87, 42, 69, 94, 39, 49, 27)
piezas_alfa={}
for i in range(9):
    piezas_alfa[i+1]=alfas[i]
piezas_beta={}
betas=(0.0005, 0.0007, 0.0004, 0.0006, 0.0009, 0.0002, 0.0005, 0.0005, 0.0007)
for i in range(9):
    piezas_beta[i+1]=betas[i]
###############################################################################
##COSTO DE INVENTARIO##
costo_inventario=(810, 1020, 510, 890, 480, 870, 780, 1050, 460)
costo_inv_pieza={}
for i in range(9):
    costo_inv_pieza[i+1]=costo_inventario[i]
###############################################################################
##LARGOS DE LAS PIEZAS##
largos_piezas=(7, 9, 10, 11, 12, 14, 15, 20, 25)
largo_cada_pieza={}
for i in range(9):
    largo_cada_pieza[i+1]=largos_piezas[i]
###############################################################################
##DATOS DE INSUMOS##
insumos=[82, 39, 41, 51, 49, 43, 90, 51, 69, 59, 86, 100, 79, 70]
promedio_insumos=round(sum(i for i in insumos)/len(insumos))
insumos.append(promedio_insumos)
###############################################################################

"""Esta función es para aquellos días en los cuales hay suficiente insumo para satisfacer los precios y demandas óptimas.
Luego, hay que decidir si guardar en inventario lo que sobra, o si se manda a astillar
inmediatamente."""

def sobra_dia_i(dia):
    m2=Model("Sobrantes")
    x = {}
    for i in indices_patrones:
        x[i] = m2.addVar(vtype=GRB.INTEGER, name="x_{0}".format(i))

    precios_cualquiera={}
    for i in indices_piezas:
        precios_cualquiera[i]=m2.addVar(lb=0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="p_{0}".format(i))

    #Función objetivo#
    m2.setObjective(sum(piezas_alfa[i]*precios_cualquiera[i]-piezas_beta[i]*precios_cualquiera[i]*precios_cualquiera[i]
    for i in indices_piezas)-sum(x[j]*costo_patron[j] for j in indices_patrones), GRB.MAXIMIZE)


    #RESTRICCIONES QUE RELACIONAN DEMANDA Y PRECIO#
    for d in indices_piezas:
        m2.addConstr(sum(x[p]*piezas_patron[p][d-1] for p in indices_patrones) == \
        (piezas_alfa[d]-piezas_beta[d]*precios_cualquiera[d]), "d_{0}".format(d))

    #TODOS LOS TRONCOS SE CORTAN#
    m2.addConstr(sum(x[i] for i in indices_patrones) <= insumos[dia])

    #OPTIMIZAMOS#
    m2.optimize()
    print('Obj: {}'.format(m2.objVal))
    utilidad_dia=m2.objVal

    #Se guarda la cantidad de patrones que se generan#
    cantidad_patrones=[]
    for v in m2.getVars():
        print("{0} {1}".format(v.varName, v.x))
        if v.varName[0]=="x":
            cantidad_patrones.append(int(v.x))


    ###Vemos cuantas piezas se generan de cada una###
    cantidad_piezas=np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
    for i in indices_patrones:
        cantidad_piezas+=cantidad_patrones[i-1]*np.array(piezas_patron[i])

    #Guardo la cantidad de troncos cortados#
    cantidad_troncos_cortados=0
    for i in cantidad_patrones:
        cantidad_troncos_cortados+=i

    #Guardo la cantidad de troncos que sobran y que no han sido cortados#
    cantidad_troncos_sobrantes=insumos[dia]-cantidad_troncos_cortados

    #Costo de inventario por patron#
    costo_inventario_patron_i=np.array([4230, 5770, 2910, 4400, 2680, 3420, 2500, 3750, 5610, 5380,
    5040, 3510, 2590, 3460, 5420, 5070, 3360, 2800, 6960, 6150, 2830])
    #Orden de los patrones más baratos de acuerdo al índice dentro de la lista#

    lista_costo_inventario_barato=[6, 12, 4, 17, 20, 2, 16, 5, 13, 11, 7, 0, 3, 10, 1, 15, 9, 14, 8, 19, 18]

    if insumos[dia+1]<44:
        if insumos[dia+1]+cantidad_troncos_sobrantes<44:
            patrones_dia_siguiente, precios_dia_siguiente, utilidad_dia_siguiente=cutting_teorico(dia+1, cantidad_troncos_sobrantes)

            patrones_insumo_sobrante=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            while cantidad_troncos_sobrantes!=0:
                for i in lista_costo_inventario_barato:
                    if patrones_dia_siguiente[i]!=0:
                        if cantidad_troncos_sobrantes-patrones_dia_siguiente[i]>0:
                            cantidad_troncos_sobrantes-=patrones_dia_siguiente[i]
                            patrones_insumo_sobrante[i]=patrones_dia_siguiente[i]
                        else:
                            patrones_insumo_sobrante[i]=cantidad_troncos_sobrantes
                            cantidad_troncos_sobrantes=0

            cantidad_piezas_sobrantes_cortadas=np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
            for i in range(len(patrones_insumo_sobrante)):
                cantidad_piezas_sobrantes_cortadas+=patrones_dia_siguiente[i]*np.array(piezas_patron[i+1])

            costos_inventario=np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
            for i in range(len(cantidad_piezas_sobrantes_cortadas)):
                costo_inventario[i]=cantidad_piezas_sobrantes_cortadas[i]*costo_inv_pieza[i+1]

            precios_siguiente_dia=np.array(precios_dia_siguiente)

            utilidad_venta_sobrante=np.dot(cantidad_piezas_sobrantes_cortadas, precios_siguiente_dia)-costos_inventario
            utilidad_astillado_sobrante=cantidad_troncos_sobrantes*71*2050-cantidad_troncos_sobrantes*costo_patron[6]

            if utilidad_vender_dia_siguiente>=utilidad_astillado_sobrante:
                return utilidad_dia
            else:
                utilidad_dia+=utilidad_astillado_sobrante
                return utilidad_dia, utilidad_dia_siguiente

        elif insumos[dia+1]+cantidad_troncos_sobrantes>=44:
            patrones_dia_siguiente, precios_dia_siguiente, utilidad_dia_siguiente=cutting_teorico(dia+1, 44-insumos[dia+1])
            cantidad_troncos_sobrantes-=abs((44-insumos[dia+1]))
            utilidad_astillado_sobrante=cantidad_troncos_sobrantes*71*2050-cantidad_troncos_sobrantes*costo_patron[6]
            utilidad_dia+=utilidad_astillado_sobrante
            return utilidad_dia, utilidad_dia_siguiente
    else:
        print("Al día siguiente no le faltan piezas")


"""Función que se utiliza para determinar el precio al cual se venden las piezas de un día cualquiera"""
def cutting_teorico(dia, troncos_recibidos):
    m2=Model("Princing día siguiente")
    x = {}
    for i in indices_patrones:
        x[i] = m2.addVar(vtype=GRB.INTEGER, name="x_{0}".format(i))

    precios_cualquiera={}
    for i in indices_piezas:
        precios_cualquiera[i]=m2.addVar(lb=0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="p_{0}".format(i))

    #Función objetivo#
    m2.setObjective(sum(piezas_alfa[i]*precios_cualquiera[i]-piezas_beta[i]*precios_cualquiera[i]*precios_cualquiera[i]
    for i in indices_piezas)-sum(x[j]*costo_patron[j] for j in indices_patrones), GRB.MAXIMIZE)


    #RESTRICCIONES QUE RELACIONAN DEMANDA Y PRECIO#
    for d in indices_piezas:
        m2.addConstr(sum(x[p]*piezas_patron[p][d-1] for p in indices_patrones) == \
        (piezas_alfa[d]-piezas_beta[d]*precios_cualquiera[d]), "d_{0}".format(d))

    #TODOS LOS TRONCOS SE CORTAN#
    m2.addConstr(sum(x[i] for i in indices_patrones) <= insumos[dia]+troncos_recibidos)

    #OPTIMIZAMOS#
    m2.optimize()
    utilidad_dia=m2.objVal
    #Se guarda la cantidad de patrones que se generan#
    cantidad_patrones=[]
    for v in m2.getVars():
        print("{0} {1}".format(v.varName, v.x))
        cantidad_patrones.append(int(v.x))


    precios=[]
    for v in m2.getVars():
        if v.varName[0]=="p":
            precios.append(v.x)

    #Guardo la cantidad de troncos cortados#
    cantidad_troncos_cortados=0
    for i in cantidad_patrones:
        cantidad_troncos_cortados+=i

    #Guardo la cantidad de troncos que sobran y que no han sido cortados#
    cantidad_troncos_sobrantes=insumos[dia]-cantidad_troncos_cortados

    ###Vemos cuantas piezas se generan de cada una###
    cantidad_piezas=np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
    for i in indices_patrones:
        cantidad_piezas+=cantidad_patrones[i-1]*np.array(piezas_patron[i])

    return cantidad_patrones, precios, utilidad_dia

def sobra_dia_i_y_siguiente(dia):
        m2=Model("Princing día siguiente")
        x = {}
        for i in indices_patrones:
            x[i] = m2.addVar(vtype=GRB.INTEGER, name="x_{0}".format(i))

        precios_cualquiera={}
        for i in indices_piezas:
            precios_cualquiera[i]=m2.addVar(lb=0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="p_{0}".format(i))

        #Función objetivo#
        m2.setObjective(sum(piezas_alfa[i]*precios_cualquiera[i]-piezas_beta[i]*precios_cualquiera[i]*precios_cualquiera[i]
        for i in indices_piezas)-sum(x[j]*costo_patron[j] for j in indices_patrones), GRB.MAXIMIZE)


        #RESTRICCIONES QUE RELACIONAN DEMANDA Y PRECIO#
        for d in indices_piezas:
            m2.addConstr(sum(x[p]*piezas_patron[p][d-1] for p in indices_patrones) == \
            (piezas_alfa[d]-piezas_beta[d]*precios_cualquiera[d]), "d_{0}".format(d))

        #TODOS LOS TRONCOS SE CORTAN#
        m2.addConstr(sum(x[i] for i in indices_patrones) <= insumos[dia])

        #OPTIMIZAMOS#
        m2.optimize()
        utilidad_dia=m2.objVal

        #Se guarda la cantidad de patrones que se generan#
        cantidad_patrones=[]
        for v in m2.getVars():
            print("{0} {1}".format(v.varName, v.x))
            cantidad_patrones.append(int(v.x))

        precios=[]
        for v in m2.getVars():
            if v.varName[0]=="p":
                precios.append(v.x)

        #Guardo la cantidad de troncos cortados#
        cantidad_troncos_cortados=0
        for i in cantidad_patrones:
            cantidad_troncos_cortados+=i

        #Guardo la cantidad de troncos que sobran y que no han sido cortados#
        cantidad_troncos_sobrantes=insumos[dia]-cantidad_troncos_cortados

        ###Vemos cuantas piezas se generan de cada una###
        cantidad_piezas=np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
        for i in indices_patrones:
            cantidad_piezas+=cantidad_patrones[i-1]*np.array(piezas_patron[i])
        return utilidad_dia

def falta_dia_i(dia):
    m2=Model("Princing día siguiente")
    x = {}
    for i in indices_patrones:
        x[i] = m2.addVar(vtype=GRB.INTEGER, name="x_{0}".format(i))

    precios_cualquiera={}
    for i in indices_piezas:
        precios_cualquiera[i]=m2.addVar(lb=0, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS, name="p_{0}".format(i))

    #Función objetivo#
    m2.setObjective(sum(piezas_alfa[i]*precios_cualquiera[i]-piezas_beta[i]*precios_cualquiera[i]*precios_cualquiera[i]
    for i in indices_piezas)-sum(x[j]*costo_patron[j] for j in indices_patrones), GRB.MAXIMIZE)


    #RESTRICCIONES QUE RELACIONAN DEMANDA Y PRECIO#
    for d in indices_piezas:
        m2.addConstr(sum(x[p]*piezas_patron[p][d-1] for p in indices_patrones) == \
        (piezas_alfa[d]-piezas_beta[d]*precios_cualquiera[d]), "d_{0}".format(d))

    #TODOS LOS TRONCOS SE CORTAN#
    m2.addConstr(sum(x[i] for i in indices_patrones) <= insumos[dia])

    #OPTIMIZAMOS#
    m2.optimize()
    utilidad_dia=m2.objVal

    #Se guarda la cantidad de patrones que se generan#
    cantidad_patrones=[]
    for v in m2.getVars():
        print("{0} {1}".format(v.varName, v.x))
        cantidad_patrones.append(int(v.x))

    precios=[]
    for v in m2.getVars():
        if v.varName[0]=="p":
            precios.append(v.x)

    #Guardo la cantidad de troncos cortados#
    cantidad_troncos_cortados=0
    for i in cantidad_patrones:
        cantidad_troncos_cortados+=i

    #Guardo la cantidad de troncos que sobran y que no han sido cortados#
    cantidad_troncos_sobrantes=insumos[dia]-cantidad_troncos_cortados

    ###Vemos cuantas piezas se generan de cada una###
    cantidad_piezas=np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
    for i in indices_patrones:
        cantidad_piezas+=cantidad_patrones[i-1]*np.array(piezas_patron[i])
    return utilidad_dia

dia=13
utilidad_final1=0
while dia>0:
    if insumos[dia]>=44 and insumos[dia+1]>=44:
        utilidad_final1+=sobra_dia_i_y_siguiente(dia)
        dia-=1
    elif insumos[dia]>=44 and insumos[dia+1]<44:
        utilidad_dia, utilidad_dia_siguiente=sobra_dia_i(dia)
        utilidad_final1+=utilidad_dia+utilidad_dia_siguiente
        dia-=2
    elif insumos[dia]<44:
        utilidad_final1+=falta_dia_i(dia)
        dia-=1

dia=13
utilidad_final2=0
while dia>0:
    utilidad_final2+=falta_dia_i(i)
    dia-=1

print(utilidad_final1, utilidad_final2)
print(utilidad_final1-utilidad_final2)
