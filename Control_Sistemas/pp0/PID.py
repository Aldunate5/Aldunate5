import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import control


plt.figure(1)
T=np.arange(0,10,0.02)
data = pd.read_csv('salida_PID.txt',sep=',\s+',header=None)
print(data)
posicion=data.iloc[:,0].values.tolist()
print(posicion)
plt.plot(T,posicion,label='GE = 2')
plt.title('Posicion vs Tiempo - Caso PID' )
plt.xlabel('Tiempo (ms)')
plt.ylabel('Angulo °')
plt.tight_layout()
plt.show()
