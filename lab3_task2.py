import numpy as np 
h=100
g=9.8
p=3.14
a=p/3
b=p/6
v= np.sqrt((g * h * np.tan(b)**2) / (2 * np.cos(a)**2 * (1 - np.tan(b) * np.tan(a))))
print(v)

from lab3_task1 import k, e, h
T=200
ε=300
p=3.14
N=(2 / np.sqrt(p)) * (h / (k * T)**(3//2)) * (e**(-ε / k * T)) * (ε ** (T/2))
print(N)