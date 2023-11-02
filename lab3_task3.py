import numpy as np 
from lab3_task1 import gravity_constant as g 

alpha = np.pi / 100 * 45

v0=10
v0x= v0 * np.cos(alpha)
v0y= v0 * np.sin(alpha)
k=0
p=0


t = np.arange(0, 5, 0.1)
x = k + v0x * t
y = p + v0y * t - ((g * t ** 2) / 2)

coord = np.zeros((len(t), 3))
for i in range(len(t)):
    coord[i, 0] = t[i]
    coord[i, 1] = x[i]
    coord[i, 2] = y[i]
print(coord)