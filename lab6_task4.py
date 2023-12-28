import matplotlib.pyplot as plt  
import numpy as np 

x = [0, r*np.cos(fi), r*np.cos(fi),  r*np.cos(fi), 0] 
y = [0, 0, r*np.sin(fi), 0] 
 
plt.plot(y, x, color='black', label='Graf 1', marker='>', ms=5) 
plt.plot(x, y, color='black', label='Graf 2', marker='o', ms=3) 
 
plt.xlabel('Coord: x') 
plt.ylabel('Coord: y') 
plt.title('Base') 
plt.axis('equal') 
plt.savefig('fig_8.png')