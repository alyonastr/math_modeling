import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10**5, 1)

def met(V, t):
    dhdt = (G * M)/ V**2 - R
    return dhdt

V_0 = 1000
R = 6371
M = 5.9736*10**24
G = 6.6743 * 10 **-11

V_t = odeint(met, V_0, t)
 
plt.plot(t, V_t[:,0], label='')
plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.legend()

plt.savefig('fig5.png')