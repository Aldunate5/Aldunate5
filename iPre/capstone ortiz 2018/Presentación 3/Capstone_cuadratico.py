from gurobipy import *
import numpy as np

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

indices_piezas = [i for i in range(1,10)]
indices_patrones = [i for i in range(1,22)]

alfas=(66, 71, 87, 42, 69, 94, 39, 49, 27)
piezas_alfa={}
for i in range(9):
    piezas_alfa[i+1]=alfas[i]
piezas_beta={}
betas=(0.0005, 0.0007, 0.0004, 0.0006, 0.0009, 0.0002, 0.0005, 0.0005, 0.0007)
for i in range(9):
    piezas_beta[i+1]=betas[i]

insumo=80

costo_patron = {}
lista_costos_patrones = [132800, 141000, 83750, 109300, 81700, 81700, 85800, 89900, 160400, 138950,
138950, 105200, 83750, 109300, 141000, 141000, 105200, 91950, 179800, 162450, 91950]
for i in indices_patrones:
    costo_patron[i] = lista_costos_patrones[i-1]

"""Se hace un nuevo pricing"""

print("El problema debe hacer un nuevo pricing")
print("#####################################################################################")
m2=Model("Nuevo pricing")
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
    piezas_alfa[d]-piezas_beta[d]*precios_cualquiera[d], "d_{0}".format(d))

#TODOS LOS TRONCOS SE CORTAN#
m2.addConstr(sum(x[i] for i in indices_patrones) <= insumo)

#OPTIMIZAMOS#
m2.optimize()

cantidad_patrones=[]
for v in m2.getVars():
    if v.varName[0] == "x":
        cantidad_patrones.append(int(v.x))

cantidad_piezas=np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
for i in range(len(cantidad_patrones)):
    cantidad_piezas+=cantidad_patrones[i]*np.array(piezas_patron[i+1])

for v in m2.getVars():
    print("{0} {1}".format(v.varName, v.x))
print(cantidad_piezas)
print('Obj: {}'.format(m2.objVal))
