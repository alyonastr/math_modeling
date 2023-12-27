import matplotlib.pyplot as plt
import numpy as np

def kvadrat(a=1, b=1, c=0):

    x1 = np.arange(1, 6, 1)
    y1 = np.arange(1,2,1)
    x2=np.arange(1,6,1)
    y2=np.arange(1,2,1)

    plt.plot(x1, y1, x2, y2, label='my kvadrat')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title('Kvadrat')
    plt.legend()
    
    plt.savefig('fig_4.png')

if __name__ == '__main__':
	kvadrat()