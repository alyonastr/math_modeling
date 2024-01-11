import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def circle_move(R, t):
    fi = np.arange(0, 2*np.pi, 0.1)
    a = np.arange(0, 20, 0.01)
    R = a*t(fi)
    return R

def animate(i):
    ball.set_data(circle_move(R=0.5, vx0=0.01, vy0=0.01, time=i))

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