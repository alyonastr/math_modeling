import numpy as np
g=9.8
def energy(m, g, h, v):
    energy=(m*g*h) + (m*v**2)/2
    return energy 

print(energy(2, 9.8, 5, 3))