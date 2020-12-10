import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import control


plt.figure(1)
data = pd.read_csv('Vel0 - lazo abierto.txt',sep='\s+',header=None)
plt.plot(data)
plt.title('Velocidad vs Tiempo - Caso Lazo Abierto' )
plt.xlabel('Tiempo (ms)')
plt.ylabel('Velocidad (RPM)')

plt.figure(2)
ref=500
kp=0.05
ki=0.001
kd=0.1
T=np.arange(0,50,0.01)


num=[ref*kd,ref*kp,ref*ki] # coeficientes del polinomios del numerador
den = [1,(1+kd),(1+kp)+ki]  # coeficientes del polinomios del denominador segundo orden
H=control.TransferFunction(num,den) #funcion de transferencia(args_polinomiales= num, den)
t,yout=control.step_response(H,T) #asignar funcion dentro del rango de tiempo

plt.plot(t,yout)

plt.grid (True)
plt.axis([0,50,0,10]) #genera largo de ejes
plt.title("Respuesta al escalon", loc='center') #se genera titulo y se hace un label
plt.xlabel("Tiempo (s)");plt.ylabel("Salida y(t)") #se generan ejes y se hace un label

plt.show()
