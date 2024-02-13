import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)

def diff_func(z, x):
    y, z = z

    dy_dx = z*y**2
    dz_dx = z/x - y*z**2
    return dy_dx, dz_dx

y_0 = 1
z_0 = -3.

z0 = y_0, z_0

sol = odeint(diff_func, z0, x)
plt.plot(x, sol[:, 1], 'g', label='y(x) ')


plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.legend()

plt.savefig('fig3.10.png')
