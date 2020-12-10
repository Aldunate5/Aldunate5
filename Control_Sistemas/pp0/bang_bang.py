import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import control


plt.figure(1)
T=np.arange(0,10,0.02)
data = pd.read_csv('salida_bang.txt',sep=',\s+',header=None)
print(data)
posicion=data.iloc[:,0].values.tolist()
print(posicion)
plt.plot(T,posicion,label='Ganancia = 2')
plt.title('Posicion vs Tiempo - Caso Bang Bang Ganancia 2' )
plt.xlabel('Tiempo (ms)')
plt.ylabel('Angulo °')
plt.tight_layout()
plt.show()

plt.figure(2)
T=np.arange(0,10,0.02)
data2 = pd.read_csv('salida_bang_2.txt',sep=',\s+',header=None)
posicion2=data2.iloc[:,0].values.tolist()
plt.plot(T,posicion2,label='Ganancia = 3')
plt.title('Posicion vs Tiempo - Caso Bang Bang Ganancia 3')
plt.xlabel('Tiempo (ms)')
plt.ylabel('Angulo °')
plt.tight_layout()
plt.show()

plt.figure(3)

T=np.arange(0,10,0.02)
plt.plot(T,posicion,label='Ganancia = 2')
plt.plot(T,posicion2,label='Ganancia = 3')
plt.title('Posicion vs Tiempo - Caso Bang Bang' )
plt.xlabel('Tiempo (ms)')
plt.ylabel('Angulo °')
plt.legend(loc="center left",bbox_to_anchor=(1,0.5)) #se genera un key de manera de identificar cada simulacion segun color
plt.tight_layout()
plt.show()

