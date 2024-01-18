import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def bumerang_move(R, angle_vel, x0, y0, xb0, yb0, t):
    t = np.arange(0, 4*np.pi, 0.1)
    alpha = angle_vel * np.pi / 180*t
    x = R*np.cos(alpha)
    y = R*np.sin(alpha)
    xb = x0*np.cos(t)-y0*np.sin(t)
    yb = y0*np.cos(t)+x0*np.sin(t)
    return x, y, xb, yb

def animate(i):
    ball.set_data(bumerang_move(R=2, angle_vel=1, x0=1, y0=1, xb0=1, yb0=1, t=i))

if __name__=='__main__':
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], '-', color='g', label='Ball')

    edge=3
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig,
                        animate,
                        frames=100,
                        interval=30)

ani.save('animation_5.gif')