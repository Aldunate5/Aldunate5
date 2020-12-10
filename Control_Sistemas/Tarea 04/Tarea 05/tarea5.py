import numpy as np
import matplotlib.pyplot as plt
import control

#### Caso C1 #####
G = control.TransferFunction([3], [1, 7, 6])
C1 = control.TransferFunction([1, 10], [1, 30.31])
K = 109.34
H1 = control.feedback(G * C1 * K)
[rlist, klist] = control.rlocus(
    H1, plotstr='-', Plot=True, PrintGain=True, grid=False)
plt.show()

t = np.arange(0, 30, 0.05)
T1, yout1 = control.step_response(H1, t)
plt.plot(T1, yout1)
plt.xlabel('Tiempo [s]'), plt.ylabel('Salida')
plt.title('Respuesta a entrada en escalon - Compensador 1')
plt.show()



C2 = control.TransferFunction([1, 0.136], [1, 0.05])
H2 = control.feedback(G * C1 * C2 * K)
#[rlist2, klist2] = control.rlocus(
#    H2, plotstr='-', Plot=True, PrintGain=True, grid=False)
#plt.show()
t = np.arange(0, 30, 0.05)
T2, yout2 = control.step_response(H2, t)
plt.plot(T2, yout2)
plt.xlabel('Tiempo [s]'), plt.ylabel('Salida')
plt.title('Respuesta a entrada en escalon - Compensador 2')
plt.show()


#comparacion
t = np.arange(0, 30, 0.05)
T1, yout1 = control.step_response(H1, t)
T2, yout2 = control.step_response(H2, t)
plt.plot(T1, yout1, label='Compensador C1')
plt.plot(T2, yout2,label='Compensador C1 + C2')
plt.xlabel('Tiempo [s]'), plt.ylabel('Salida')
plt.title('Respuesta a entrada en escalon - Comparacion')
plt.legend(loc="center left",bbox_to_anchor=(1,0.5)) #se genera un key de manera de identificar cada simulacion segun color
plt.tight_layout() #se ajusta legend al ancho de la pantalla
plt.show()

print(control.step_info(H1))

print(control.step_info(H2))
