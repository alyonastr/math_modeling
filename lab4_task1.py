import numpy as np 
def mult_func(array):
    s=0
    for i in range(len(array)):
        s += array[i]
    return s/len(array)

test = np.arange(0,100,1)
print(mult_func(test))
