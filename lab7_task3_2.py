import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def bumerang_move(R, angle_vel, vx0, vy0, vbx0, vby0, t):
    alpha = angle_vel * np.pi / 360*t

    x0 = vx0 * t
    y0 = vy0 * t
    x = x0 + R*np.cos(alpha)
    y = y0 + R*np.sin(alpha)

    xb0 = vbx0 * t
    yb0 = vby0 * t
    xb = xb0*np.cos(t)-yb0*np.sin(t)
    yb = yb0*np.cos(t)+xb0*np.sin(t)
    return x, y, xb, yb

def animate(i):
    ball.set_data(bumerang_move(R=2, angle_vel=9, vx0=1, vy0=1, vbx0=1, vby0=1, t=i))

if __name__=='__main__':
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], '--', color='g', label='Ball')

    edge=3
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig,
                        animate,
                        frames=360,
                        interval=30)

ani.save('animation_5.gif')