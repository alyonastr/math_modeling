import matplotlib.pyplot as plt 
import numpy as np 

def cikloida(R=3,t=4):
    

    x = R*(t-((np.sin)**3)*t)
    y = R*(1-((np.cos)**3)*t)

    plt.plot(x,y, ls='--', lw=3)
    plt.axis('equal')
    plt.savefig('fig_5.png')

if __name__=='__main__':
    cikloida()