import matplotlib.pyplot as plt  
import numpy as np  
 
def giperbola_plotter(R=1, t=4): 

    x = np.arange(-10, 10, 0.1) 
    y = np.arange(-10, 10, 0.1) 
    x = R*(t-(np.sin**3)*t)
    y = R*(1-(np.cos**3)*t)
 
    plt.plot(x, y, label='My giperbola') 
    plt.xlabel('Coord - x') 
    plt.ylabel('Coord - y') 
    plt.title('Giperbola') 
    plt.legend() 
     
    plt.savefig('fig_4.png') 
 
if __name__=='__main__': 
    giperbola_plotter()
