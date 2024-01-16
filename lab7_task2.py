import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def circle_move(R, t):
    fi = np.arange(0, 2*np.pi, 0.1)
    t = np.arange(0, 20, 0.01)
    a = np.arange(0, 5, 1)
    R = a*t
    x =R*np.cos(fi)
    y =R*np.sin(fi)
    return R

def animate(i):
    ball.set_data(circle_move(R,t=i))

if __name__=='__main__':
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], 'o', color='y', label='Ball')

    edge=3
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig,
                        animate,
                        frames=180,
                        interval=30)

ani.save('animation_4.gif')