import numpy as np 
def func(array):
    r=1
    for i in range(len(array)):
        r *= array[i]
    return r

test = np.arange(1,6,1)
print(func(test))