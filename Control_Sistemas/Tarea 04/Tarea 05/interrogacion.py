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