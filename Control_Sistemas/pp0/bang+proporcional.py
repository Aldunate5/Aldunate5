import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import control



data = pd.read_csv('salida_proporcional0.5.txt',sep=',\s+',header=None)
posicion=data.iloc[:,0].values.tolist()

data = pd.read_csv('salida_bang.txt',sep=',\s+',header=None)
posicion2=data.iloc[:,0].values.tolist()



plt.figure(1)

T=np.arange(0,10,0.02)
plt.plot(T,posicion,label='Proporcional')
plt.plot(T,posicion2,label='Bang Bang')
plt.title('Posicion vs Tiempo - Comparacion' )
plt.xlabel('Tiempo (ms)')
plt.ylabel('Angulo °')
plt.legend(loc="center left",bbox_to_anchor=(1,0.5)) #se genera un key de manera de identificar cada simulacion segun color
plt.tight_layout()
plt.show()