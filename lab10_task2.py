import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1, 1, 0.001)

def diff_func(z, t):
    x, y = z

    dx_dt = 3*x - 2*y + (e**(3*t)/e*t + 1)
    dy_dt = x - (np.e**(3*t) /e*t + 1)
    return dx_dt, dy_dt

x_0= 5
y_0 = -7
e = 2.71828182846
z0 = x_0, y_0



sol = odeint(diff_func, z0, t)
plt.plot(t, sol[:, 1], 'g', label='y(t) ')


plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.legend()

plt.savefig('fig4.10.png')
