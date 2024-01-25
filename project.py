from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


def circle_move(alpha):
    t = np.arange(0, 4*np.pi, 0.1)
    x = 12*np.cos(t) + 8*np.cos(1.5*t)
    y = 12 * np.sin(t) - 8*np.sin(1.5*t)
    R=1000

    X0= R * np.cos(alpha*10)
    Y0= R * np.sin(alpha*10)

    X = x * np.cos(alpha) - y * np.sin(alpha) + X0
    Y = y * np.cos(alpha) + x * np.sin(alpha) + Y0
    return X, Y


def animate(alpha):
    ball.set_data(circle_move(alpha=alpha))


if __name__ == '__main__':

    fig, ax = plt.subplots()
    ball, = plt.plot([], [], '-', color='r', label='Ball')

    edge = 100
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)
    
    ani = FuncAnimation(fig,
                        animate,
                        frames=np.arange(0, 8*np.pi, 0.01),
                        interval=30
                       )

    ani.save('test.gif') 