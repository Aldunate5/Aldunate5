import amplpy
import pandas as pd
import Generar_Dataframe
"""
•	hold{F}; costo de inventario de producto final f
•	alfa{F}; Maximo valor de demanda para producto final f
•	beta{F}; (sensibilidad precio demanda): tasa de variación de demanda producto del cambio en precio de producto final
•	precio{F}; precio de producto final
•	c_cut{K}; costo de cortar una pieza entera
•	insumos{T}; materia prima a procesar por día t
•	n_cuts{F,K}; cantidad de productos finales f obtenidos por patron de corte k
•	Inv_I{F,Delta}; Inventario inicial y su caducidad inicial
•	delta1 = 14; vencimiento: puede ser modificable
•	TF=30; final de horizonte de evaluacion
•	apren{K};
•	por_ap{K};
"""

def hold_corte(hold,modificable_hold):
    hold=hold['hold']
    for idx, recorrido in enumerate(modificable_hold):
        hold[idx] += recorrido
    new_hold=hold
    return new_hold

def max_demanda(alpha,modificable_alpha):
    alpha=alpha['alfa']
    for idx, recorrido in enumerate(modificable_alpha):
        alpha[idx] += recorrido
    new_alpha=alpha
    return new_alpha

def tasa_demanda(beta,modificable_beta):
    beta=beta['beta']
    for idx, recorrido in enumerate(modificable_beta):
        beta[idx] += recorrido
    new_beta=beta
    return new_beta

