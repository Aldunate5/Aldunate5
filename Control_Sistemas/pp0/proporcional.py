import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import control


plt.figure(1)
T=np.arange(0,10,0.02)
data = pd.read_csv('salida_proporcional0.5.txt',sep=',\s+',header=None)
print(data)
posicion=data.iloc[:,0].values.tolist()
print(posicion)
plt.plot(T,posicion,label='GE = 2')
plt.title('Posicion vs Tiempo - Caso Proporcional Kp=0.5' )
plt.xlabel('Tiempo (ms)')
plt.ylabel('Angulo °')
plt.tight_layout()

plt.figure(2)
T=np.arange(0,10,0.02)
data2 = pd.read_csv('salida_proporcional0.1.txt',sep=',\s+',header=None)
posicion2=data2.iloc[:,0].values.tolist()
plt.plot(T,posicion2,label='GE = 2')
plt.title('Posicion vs Tiempo - Caso Proporcional Kp=0.1' )
plt.xlabel('Tiempo (ms)')
plt.ylabel('Angulo °')
plt.tight_layout()


plt.figure(3)
T=np.arange(0,10,0.02)
plt.plot(T,posicion,label='Kp = 0.5')
plt.plot(T,posicion2,label='Kp = 0.1')
plt.title('Posicion vs Tiempo - Caso Proporcional' )
plt.xlabel('Tiempo (ms)')
plt.ylabel('Angulo °')
plt.legend(loc="center left",bbox_to_anchor=(1,0.5)) #se genera un key de manera de identificar cada simulacion segun color
plt.tight_layout()
plt.show()