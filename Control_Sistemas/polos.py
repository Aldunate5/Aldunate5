import control
import numpy as np
import matplotlib.pyplot as plt

#z=0.5, wn=1

T=np.arange(0,50,0.01)
polos=[0.1,0.5,0.8,1,2,5,10]


for a in polos:
    num=[1] # coeficientes del polinomios del numerador
    #den=[1,(1+a),(1+a),a] # coeficientes del polinomios del denominador
    #den = [1, a]  # coeficientes del polinomios del denominador primer orden
    den = [1,1,1]  # coeficientes del polinomios del denominador segundo orden
    H=control.TransferFunction(num,den) #funcion de transferencia(args_polinomiales= num, den)

    t,yout=control.step_response(H,T) #asignar funcion dentro del rango de tiempo

    plt.plot(t,yout,label=("Polo = "+str(a)))

plt.grid (True)
plt.axis([0,50,0,1.5]) #genera largo de ejes
plt.title("Respuesta al escalon", loc='center') #se genera titulo y se hace un label
plt.xlabel("Tiempo (s)");plt.ylabel("Salida y(t)") #se generan ejes y se hace un label
plt.legend(loc="center left",bbox_to_anchor=(1,0.5)) #se genera un key de manera de identificar cada simulacion segun color
plt.tight_layout() #se ajusta legend al ancho de la pantalla
plt.show()
