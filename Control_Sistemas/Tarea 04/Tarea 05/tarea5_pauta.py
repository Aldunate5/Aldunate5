import numpy
import matplotlib
import control
from pylab import *
from numpy import *
from scipy import signal

G = control.TransferFunction([6], [1, 7, 6])
C1 = control.TransferFunction([1, 10], [1, 30.31])
K = 54.67
H1 = control.feedback(G * C1 * K)
C2 = control.TransferFunction([1, 0.13583], [1, 0.05])
H2 = control.feedback(G * C1 * C2 * K)
[rlist, klist] = control.rlocus(
    H1, kvect=None, xlim=None, ylim=None, plotstr='-', Plot=True, PrintGain=True, grid=False)
# plt.show()
[rlist2, klist2] = control.rlocus(
    H2, kvect=None, xlim=None, ylim=None, plotstr='-', Plot=True, PrintGain=True, grid=False)
# plt.show()
# Parte 2: Respuesta ante escalon
t = arange(0, 25, 0.01)
T1, yout1 = control.step_response(H1, t)
T2, yout2 = control.step_response(H2, t)
plot(T1, yout1, label='Sistema realimentado con C1')
plot(T2, yout2, label='Sistema realimentado con C1 y C2')
xlabel('Tiempo [s]')
ylabel('Salida')
title('Respuesta en el tiempo de una senal tipo escalon')

# plt.show()
# Tiempo establecimiento
n = len(yout1) - 1
ts = 0
while (n > 0):
    n = n - 1
    if (abs(yout1[n] - yout1[-1]) > 0.01):
        ts = T1[n]
        break
print("Tiempo de Establecimiento:", ts)

# Sobreoscilacion
Mp = ((max(yout1) - yout1[-1]) / (yout1[-1]) * 100)
print("Sobreoscilacion:", Mp, '%')


# Tiempo Peak
tp = 0
for i in arange(len(yout1)):
    if (yout1[i] == max(yout1)):
        tp = T1[i]
        break
print("Tiempo Peak", tp)

# tiempo de subida
tiempor1 = 0
tiempor2 = 0
for i in arange(len(yout1)):
    if (yout1[i] >= 0.9 * yout1[-1]):
        tiempor1 = T1[i]
        break
for i in arange(len(yout1)):
    if (yout1[i] >= 0.1 * yout1[-1]):
        tiempor2 = T1[i]
        break
tr = tiempor1 - tiempor2
print("Tiempo de subida:", tr)

ep = 1 - yout1[-1]
print('error promedio:', ep)
