import matplotlib.pyplot as plt  
import numpy as np 

def circle_plotter(b=10, k=4, ):
    
    x = np.arange(-2*r, 2*r, 0.1)
    y = np.arange(-2*r, 2*r, 0.1)

   
    X, Y = np.meshgrid(x, y)

    

    plt.contour(X, Y, fxy, levels=[0])
    plt.axis('equal')
    
    plt.savefig('fig_4.png')
    
if __name__ == '__main__':
	circle_plotter()