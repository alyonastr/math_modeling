import matplotlib.pyplot as plt 
import numpy as np 

def cikloida(R=3, t=5):
    alpha=np.sin(t)**3
    beta=np.cos(t)**3
    x = R*(t-alpha)
    y = R*(1-beta)

    plt.plot(x,y, ls='--', lw=3)
    plt.axis('equal')
    plt.savefig('fig_5.png')

if __name__=='__main__':
    cikloida()


