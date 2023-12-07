import numpy as np 
a=10
b=30
c=[]
def y(x):
    for i in range (a,b):
        y=x**2
        c.append(y)
    return c

res=y(5)
print(res)