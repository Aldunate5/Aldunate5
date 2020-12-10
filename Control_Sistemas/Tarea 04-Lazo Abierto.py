import numpy as np
import matplotlib.pyplot as plt
import control

#funcion de transferencia lazo abierto
num=[1]
den=[1,2,2,1]
G=control.TransferFunction(num,den)


T=np.arange(0,10,0.05)
T,yout=control.step_response(G,T)
plt.title('Salida del Sistema G(s)')
plt.xlabel("Tiempo (s)");plt.ylabel("Salida y(t)")
plt.plot(T,yout)
plt.show()


#R y L del grafico
R=0.386
L=0.9

#Ziegler-Nichols
kp=1.2/(R*L)
ki=kp/(2*L)
kd=kp*(L/2)
print(kp,ki,kd)

#Funcion del controlador
num_d=[kd,kp,ki]
den_d=[1,0]
D=control.TransferFunction(num_d,den_d)

#Funcion lazo abierto
H=control.feedback(G*D)

#Grafico
T=np.arange(0,10,0.05)
T,yout=control.step_response(H,T)

plt.title('Salida del sistema H(s)')
plt.xlabel("Tiempo (s)");plt.ylabel("Salida y(t)")
plt.plot(T,yout)
plt.show()

print(control.step_info(H))