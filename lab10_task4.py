import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-5, 5, 0.001)

def diff_func(z, t):
    y, omega = z

    dy_dt = omega
    domega_dt = -4*omega - 5*y
    return dy_dt, domega_dt

y_0 = 4
omega0 = -1.

z0 = y_0, omega0

sol = odeint(diff_func, z0, t)
plt.plot(t, sol[:, 1], 'g', label='y(t) ')


plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.legend()

plt.savefig('fig6.10.png')
