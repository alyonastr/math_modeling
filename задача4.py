import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

frames = 200
t = np.linspace(0, 5, frames)

def move_func(z, t):
    x, v_x, y, v_y = z 
    dxdt = v_x
    dv_xdt = - gamma * vv_x * np.cos(beta) - kappa * v_x
    dydt = v_y
    dv_ydt = gamma * vv_y * np.sin(beta) - g - kappa * v_y
    return dxdt, dv_xdt, dydt, dv_ydt

g = 9.8
v = 15
gamma = 0.1
m = 1
vv = 20 
beta = 30 * np.pi / 180
alpha = 80 * np.pi / 180
kappa = 0.3

x0 = 0
v_x0 = v * np.cos(alpha)
y0 = 0
v_y0 = v * np.sin(alpha)

vv_x = vv * np.cos(beta)
vv_y = vv * np.sin(beta)


z0 = x0, v_x0, y0, v_y0

sol = odeint(move_func, z0, t)
def solve_func(i, key):
    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]
    else: 
        x = sol[:i, 0]
        y = sol[:i, 2]
    return x, y

fig, ax = plt.subplots()

ball, = plt.plot( [], [], 'o', color='r')
ball_line, = plt.plot( [], [], '-', color='r')

def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

edge = 15
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)

ani.save('gif4.gif')
