import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10**5, 1)

def met(g, t):
    dgdh = k * M
    return didt

g_0 = 2
k = 6.6743 * 10**11 
M = 5.9736*10**24

G = odeint(met, M, t)
 
plt.plot(t, g[:,0], label='')
plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.legend()

plt.savefig('fig5.png')