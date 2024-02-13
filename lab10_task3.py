import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.001)

def diff_func(z, x):
    y, omega = z

    dy_dx = omega
    domega_dx = np.sin(x)+ np.cos(x)
    return dy_dx, domega_dx

y_0 = 3
omega_0 = 0
z0 = y_0, omega_0

sol = odeint(diff_func, z0, x)
plt.plot(x, sol[:, 1], 'g', label='y(x) ')


plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.legend()

plt.savefig('fig5.10.png')
