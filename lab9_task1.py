import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 500, 0.1)

def bact(N, t):
    dNdt = k * N
    return dNdt

N_0 = 1
k = 5 * 10**(-2) 

N_t = odeint(bact, N_0, t)
 
plt.plot(t, N_t[:,0], label='')
plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.legend()

plt.savefig('fig2.png')