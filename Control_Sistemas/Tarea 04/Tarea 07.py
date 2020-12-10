import numpy
import matplotlib
import control
from pylab import *
from numpy import *
from scipy import signal



G = control.TransferFunction([2], [1, 1])
H = G / (1 + G)
t = arange(0, 10000, 1)
T, yout1 = control.step_response(H, t)
Rramp = t
T, youtr1, xoutr1 = control.forced_response(H, T=t, U=Rramp)


error0 = (t[-1] - youtr1[-1]) / t[-1]
print("Error permanente G:", error0)

plot(T, yout1, lw=1, label="G")

plot(T, t, lw=1, label="Rampa (input)")

Gc = control.TransferFunction([1, 25], [1])
H2 = G * Gc / (1 + G * Gc)
T, youtr2, xoutr2 = control.forced_response(H2, T=t, U=Rramp)
plot(T, youtr2, lw=1, label="G*Gc")

Gc1 = control.TransferFunction([0.2233, 1], [0.087, 1])
H3 = G * Gc * Gc1 / (1 + G * Gc * Gc1)
T, youtr3, xoutr3 = control.forced_response(H3, T=t, U=Rramp)
plot(T, youtr3, lw=1, label="G*Gc*Gc1 (adelanto)")

Gc2 = control.TransferFunction([4.6897, 1], [46.897, 1])
H4 = G * Gc * Gc2 / (1 + G * Gc * Gc2)
T, youtr4, xoutr4 = control.forced_response(H4, T=t, U=Rramp)
plot(T, youtr4, lw=1, label="G*Gc*Gc2 (atraso)")

ax = plt.subplot(111)
chartBox = ax.get_position()
ax.set_position([chartBox.x0, chartBox.y0,
                 chartBox.width * 0.55, chartBox.height])  # posición externa de la leyenda (encontrado en internet)
ax.legend(loc='upper center', bbox_to_anchor=(1.5, 0.8), shadow=True, ncol=1)
xlabel('Tiempo [s]')
ylabel('Salida')
title('Respuestas en el tiempo entrada tipo rampa')
grid(True)
plt.show()


error1 = (t[-1] - youtr2[-1]) / t[-1]
error_adel = (t[-1] - youtr3[-1]) / t[-1]
error_atra = (t[-1] - youtr4[-1]) / t[-1]
print("Error permanente G*Gc:", error1)
print("Error permanente G*Gc*Gc1:", error_adel)
print("Error permanente G*Gc*Gc2:", error_atra)