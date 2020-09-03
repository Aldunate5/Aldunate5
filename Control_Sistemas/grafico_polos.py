import control
import numpy as np
import matplotlib.pyplot as plt

#z=0.5, wn=1

T=np.arange(0,50,0.01)
polos=[0.1,0.5,0.8,1,2,5,10]


for a in polos:
    num=[a] # coeficientes del polinomios del numerador
    den=[1,(1+a),(1+a),a] # coeficientes del polinomios del denominador

    H=control.TransferFunction(num,den) #funcion de transferencia(args_polinomiales= num, den)
    T = np.arange(0, 50, 0.01)

    control.pzmap(H,True,False,"Mapa de Polos Caso "+str(a))

plt.axis([-6,0,0,10])
plt.show()
