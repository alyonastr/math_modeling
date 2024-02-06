import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 6, 1)

def inv(i, t):
    didt = k * i * t
    return didt

i_0 = 1000
k = 0.08 

i_t = odeint(inv, i_0, t)
 
plt.plot(t, i_t[:,0], label='')
plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.legend()

plt.savefig('fig3.png')