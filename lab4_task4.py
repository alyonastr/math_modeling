import numpy as np 
a=10
b=30
def y(a, b, N):
    x=np.linspace(a, b, N)
    yn=x**2
    return yn

print(y(3,5,2))