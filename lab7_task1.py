import matplotlib.pyplot as plt 
import numpy as np 

def cikloida(R=3):
    t = np.arange(0, 20, 0.01)
    x = R*(t-np.sin(t))
    y = R*(1-np.cos(t))
    x1= R*np.cos(t)
    y1= R*np.sin(t)

    plt.plot(x,y,x1,y1, ls='--', lw=3)
    plt.axis('equal')
    plt.savefig('fig_5.png')

if __name__=='__main__':
    cikloida()


