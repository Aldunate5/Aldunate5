import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import scipy.stats as st


phi = ''

# rad / s

#compensador de adelanto
'''
num = [0.22*63.5,63.5]
den = [0.139,1]
'''
#compensador adelanto, sistema
'''
num = [0.22*63.5,63.5]
den = [0.139,1.556,4,0]
'''

#compensador de atraso
'''
num = [3.45*14.28,14.28]
den = [10,1]
'''
#compensador atraso, sistema

num = [3.45*14.28,14.28]
den = [10,41,4,0]


sys1 = signal.lti(num,den) # Creamos el sistema
w, mag, phase = signal.bode(sys1) # Diagrama de bode: frecuencias, magnitud y fase
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6))

ax1.grid(True,which='both'), ax1.set_title('Magnitud')
ax1.semilogx(w, mag) # Eje x logarítmico
ax1.set_ylabel('Mb',size = 15,rotation=0)
plt.xlim([0.001,100])


ax2.grid(True,which='both'), ax2.set_title('Fase')
ax2.semilogx(w, phase) # Eje x logarítmico
ax2.set_ylabel("$\\phi$".format(phi),size = 15,rotation=0)

plt.xlim([0.01,100])
plt.show()



#plt.plot(w,y)
#plt.xscale('log')
#plt.grid(True,which='both')
#plt.show()