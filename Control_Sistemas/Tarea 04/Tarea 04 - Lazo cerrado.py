import numpy as np
import matplotlib.pyplot as plt
import control

#funcion de transferencia lazo abierto
num=[1]
den=[1,2,2,1]
G=control.TransferFunction(num,den)

#Parametros de busqueda
kp=3
kd=0
ki=0

num_d=[kd,kp,ki]
den_d=[1,0]


D=control.TransferFunction(num_d,den_d)
H=G*D/(1+G*D*1)
T=np.arange(0,10,0.05)
T,yout=control.step_response(H,T)

plt.xlabel("Tiempo (s)");plt.ylabel("Salida y(t)")
plt.title('Salida del sistema H(s) busqueda')
plt.plot(T,yout)
plt.show()

########## ZN ###############

#Parametros del sistema
ku=3
tu=6
kp=0.6*ku
ki=ku/(0.5*tu)
kd=0.6*ku*(tu/8)

num_d=[kd,kp,ki]
den_d=[1,0]
D=control.TransferFunction(num_d,den_d)


#Funcion lazo cerrado
H=G*D/(1+G*D*1)


#Grafico
T=np.arange(0,10,0.05)
T,yout=control.step_response(H,T)

plt.xlabel("Tiempo (s)");plt.ylabel("Salida y(t)")
plt.title('Salida del sistema')
plt.plot(T,yout)
plt.show()

print(control.step_info(H))