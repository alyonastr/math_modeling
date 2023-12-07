import numpy as np 

def square(figure, *args):
    if figure == 'круг':
        pl=3.14*(args[0]**2)
    if figure == 'квадрат':
        pl=args[0]*args[1]
    if figure == 'треугольник':
        pl=(args[0]*args[1])/2
    return pl

print(square('круг', 6, 9))