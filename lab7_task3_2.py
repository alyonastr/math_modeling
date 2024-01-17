import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def circle_move(x0, y0, vx0, vy0, t):
    t = np.arange(0, 4*np.pi, 0.1)
    x0 = 12*np.cos(t)+ 8*np.cos(1.5*t)
    y0 = 12*np.sin(t)- 8*np.cos(1.5*t)
    x = x0*np.cos(t)-y0*np.sin(t)
    y = y0*np.cos(t)+x0*np.sin(t)
    return x, y

def animate(i):
    ball.set_data(circle_move(x0=np.arange(-25, 25, 1), y0=np.arange(-25, 25, 1), vx0=0.01, vy0=0.01, t=i))

if __name__=='__main__':
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], '-', color='y', label='Ball')

    edge=3
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig,
                        animate,
                        frames=180,
                        interval=30)

ani.save('animation_3.gif')