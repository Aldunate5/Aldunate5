import numpy as np
import matplotlib.pyplot as plt
import control

K=1
t = np.arange(0, 30, 0.01)

#Lazo Abierto
G1 = control.TransferFunction([1], [0.5, 1.5, 1])
T1, yout1 = control.step_response(G1, t)


G2 = control.TransferFunction([-0.25,1], [0.125,0.875, 1.75, 1])
T2, yout2 = control.step_response(G2, t)

plt.plot(T1, yout1,label='Lazo Abierto SR')
plt.xlabel('Tiempo [s]'), plt.ylabel('Salida')
plt.plot(T2, yout2,label='Lazo Abierto CR')
plt.xlabel('Tiempo [s]'), plt.ylabel('Salida')
plt.legend(loc="center left",bbox_to_anchor=(1,0.5)) #se genera un key de manera de identificar cada simulacion segun color
plt.tight_layout() #se ajusta legend al ancho de la pantalla
plt.title('Lazo Abierto')
plt.show()

#lazo Cerrado
#Lazo Cerrado sin retardo
G1C=G1*K/(1+G1*K)
T1C, yout1C = control.step_response(G1C, t)
plt.plot(T1C, yout1C, label='Lazo Cerrado SR')

G2C=control.feedback(G2)
T2C, yout2C = control.step_response(G2C, t)
plt.plot(T2C, yout2C, label='Lazo Cerrado CR')

plt.xlabel('Tiempo [s]'), plt.ylabel('Salida')
plt.title('Lazo Cerrado')
plt.legend(loc="center left",bbox_to_anchor=(1,0.5)) #se genera un key de manera de identificar cada simulacion segun color
plt.tight_layout() #se ajusta legend al ancho de la pantalla
plt.show()

print(control.step_info(G1))
