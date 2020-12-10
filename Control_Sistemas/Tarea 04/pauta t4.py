import control # libreria de control
import numpy as np
import matplotlib.pyplot as plt

# Metodo en lazo abierto
# LAZO ABIERTO
Kp=3.45
Ki=1.92
Kd=1.55
# Plant
G1 = control.TransferFunction([1],[1,1,1])
G2 = control.TransferFunction([1],[1,1])
G= G1*G2
print(G)
# Lazo cerrado (PID)
D = control.TransferFunction([Kd,Kp,Ki],[1,0])
H = control.feedback(D*G)
print(H)

#Caracteristicas en el tiempo lazo abierto
t = np.arange (0 ,15 ,0.001) #Rango de tiempo
to , y = control.step_response(H,t) #Respuesta al escalon
# Encontramos los puntos criticos de la respuesta del sistema
ind1a = np.where(y>=0.1)[0][0] # Inidice cuando la respuesta llega al 10 %
ind1b = np.where(y>=0.9)[0][0] # Inidice cuando la respuesta llega al 90 %
ind2 = np.argmax(y) # Inidice cuando la respuesta llega al maximo
ind3 = np.where(abs(y-1.)>0.01)[-1][-1] # Inidice cuando la respuesta llega al 1 % del valor final
# Graficamos los puntos criticos para comprobar:
plt.plot(to ,y,lw =3)
plt.grid(True)
plt.plot(t[ind1a],y[ind1a],"o",ms =10)
plt.plot(t[ind1b],y[ind1b],"o",ms =10)
plt.plot(t[ind2],y[ind2],"o",ms =10)
plt.plot(t[ind3],y[ind3],"o",ms =10)
plt.xlabel("Tiempo [s]",fontsize =18)
plt.ylabel("Salida $y(t)$",fontsize =18)
# Reportamos las caracteristicas en el tiempo
print("Tr = "+str(t[ind1b]-t[ind1a ]) + " s")
print("Tp = "+str(t[ind2 ]) + " s")
print("Mp = "+str(int(10*(max(y)*100.-100.))/10.)+" %")
print("Ts = "+str(t[ind3 ]) + " s")
print("Error permanente = 0")

'''
# Metodo en lazo cerrado
Kp=1.8
Ki=0.6
Kd=1.35
# Plant
G1 = control.TransferFunction([1],[1,1,1])
G2 = control.TransferFunction([1],[1,1])
G= G1*G2
print(G)
# Lazo cerrado (PID)
D = control.TransferFunction([Kd,Kp,Ki],[1,0])
H = control.feedback(D*G)
print(H)
#Caracteristicas en el tiempo lazo abierto
t = np.arange (0 ,15 ,0.001) #Rango de tiempo
to , y = control.step_response(H,t) #Respuesta al escalon
# Encontramos los puntos criticos de la respuesta del sistema
ind1a = np.where(y>=0.1)[0][0] # Inidice cuando la respuesta llega al 10 %
ind1b = np.where(y>=0.9)[0][0] # Inidice cuando la respuesta llega al 90 %
ind2 = np.argmax(y) # Inidice cuando la respuesta llega al maximo
ind3 = np.where(abs(y-1.)>0.01)[-1][-1] # Inidice cuando la respuesta llega al 1 % del valor final
# Graficamos los puntos criticos para comprobar:
plt.plot(to ,y,lw =3)
plt.grid(True)
plt.plot(t[ind1a],y[ind1a],"o",ms =10)
plt.plot(t[ind1b],y[ind1b],"o",ms =10)
plt.plot(t[ind2],y[ind2],"o",ms =10)
plt.plot(t[ind3],y[ind3],"o",ms =10)
plt.xlabel("Tiempo [s]",fontsize =18)
plt.ylabel("Salida $y(t)$",fontsize =18)
# Reportamos las caracteristicas en el tiempo
print("Tr = "+str(t[ind1b]-t[ind1a ]) + " s")
print("Tp = "+str(t[ind2 ]) + " s")
print("Mp = "+str(int(10*(max(y)*100.-100.))/10.)+" %")
print("Ts = "+str(t[ind3 ]) + " s")
print("Error permanente = 0")
'''