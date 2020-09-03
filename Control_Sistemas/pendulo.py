import numpy as np
import matplotlib.pyplot as plt

# Definir la salida para el impulso y el escalon
t = np.arange (0 ,5 ,0.01) # 5 s, en intervalos de 0.05 s
#0 grados
theta1 = (360/(2*3.14))*(0.22576)*np.sin(4.4294*t) # Caso: Impulso en grados
theta2 = (360/(2*3.14))*0.05096*(1-np.cos(4.4294*t)) # Caso: Escalon en grados
#30 grados
#theta1 = (360/(2*3.14))*(0.24259)*np.sin(4.12206*t) # Caso: Impulso en grados
#theta2 = (360/(2*3.14))*0.05885*(1-np.cos(4.12206*t)) # Caso: Escalon en grados
# Graficar
plt.plot(t,theta1, label = "Caso: Impulso")
plt.plot(t,theta2, label = "Caso: Escalon")
plt.grid (True)

plt.axis([0,5,-50,50]) #genera largo de ejes
plt.title("Pendulo Invertido", loc='center') #se genera titulo y se hace un label
plt.xlabel("Tiempo (s)");plt.ylabel("Posicion Angular (rad)") #se generan ejes y se hace un label
plt.legend(loc="center left",bbox_to_anchor=(1,0.5)) #se genera un key de manera de identificar cada simulacion segun color
plt.tight_layout() #se ajusta legend al ancho de la pantalla
plt.show()