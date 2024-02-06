import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 20, 1)

def mt(V, t):
    dVdt = g - y*(V**2)
    return dVdt

V_0 = 10
y = 0.2
g = 9.8

V_t = odeint(mt, V_0, t)
 
plt.plot(t, V_t[:,0], label='')
plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.legend()

plt.savefig('fig4.png')