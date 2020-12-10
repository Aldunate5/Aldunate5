import numpy as np
import matplotlib
import control
from pylab import *
from numpy import *


#caso G(s)
G = control.TransferFunction([1], [0.5, 1])
H = G / (1 + G) #Sistema realimentado
t = np.arange(0, 8, 0.01)
T, yout1 = control.step_response(H, t) #Respuesta ante impulso

T, youtr1, xoutr1 = control.forced_response(H, T=t, U=t) #Simulación para rampa
error0 = (t[-1] - youtr1[-1]) / t[-1] #se obtiene error para ultimo valor del array
print(error0,control.step_info(H,t))

plot(T, yout1)
xlabel('Tiempo [s]'), ylabel('Salida'), title('Respuesta')
plt.show()


#G*D_0
G=control.TransferFunction([50], [0.5,1,0]) #G*D_0
H2=G / (1 + G) #Sistema realimentado
t = np.arange(0, 8, 0.01)
T, yout1 = control.step_response(H2, t)

X, youtr1, xoutr1 = control.forced_response(H2, T=t, U=t) #Simulación para rampa
error0 = (t[-1] - youtr1[-1]) / t[-1] #se obtiene error para ultimo valor del array
print(error0,control.step_info(H2,t))

plot(T, yout1)
xlabel('Tiempo [s]'), ylabel('Salida'), title('Respuesta')
plt.show()


#G*D_0*D1
G=control.TransferFunction([10.5,50], [0.0245,0.549,1,0]) #G*D_0*D1
H3=G / (1 + G) #sistema retroalimentado
t = np.arange(0, 8, 0.01)
T, yout1 = control.step_response(H3, t)

T, youtr1, xoutr1 = control.forced_response(H3, T=t, U=t) #Simulación para input rampa
error0 = (t[-1] - youtr1[-1]) / t[-1] #error para ultimo valor del array
print(error0,control.step_info(H3,t))

plot(T, yout1)
xlabel('Tiempo [s]'), ylabel('Salida'), title('Respuesta')
plt.show()

#G*D_0*D2
G=control.TransferFunction([297.5,50], [67.8,136.1,1,0]) #G*D_0*D2
H3=G / (1 + G) #sistema retroalimentado
t = np.arange(0, 8, 0.01)
T, yout1 = control.step_response(H3, t)

T, youtr1, xoutr1 = control.forced_response(H3, T=t, U=t) #Simulación para input rampa
error0 = (t[-1] - youtr1[-1]) / t[-1] #error para ultimo valor del array
print(error0,control.step_info(H3,t))

plot(T, yout1)
xlabel('Tiempo [s]'), ylabel('Salida'), title('Respuesta')
plt.show()