import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

r = np.arange(6471000, 637100000, 100)

def met(V, r):
    dVdr = (G * M)/ (V * r**2)
    return dVdr

V_0 = 0.1
M = 5.9736*10**24
G = 6.6743 * 10 **(-11)


V_r = odeint(met, V_0, r)
print(V_r)
 
plt.plot(r, V_r[:,0], label='')
plt.xlabel('')
plt.ylabel('')
plt.xlim(0, 637100000)
plt.ylim(0, 637100000)
plt.title('')
plt.legend()

plt.savefig('fig5.png')