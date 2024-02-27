import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 500, 0.1)

def bact(S, t):
    dSdt = k * np.sqrt(S / np.pi) * E * S * np.cos((np.pi/12)*(t - 12))
    return dSdt

S_0 = 1600
k = 340 * 10**(-8)
E = 1360

S_t = odeint(bact, S_0, t)
 
plt.plot(t, S_t[:,0], label='')
plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.legend()

plt.savefig('fig6.png')