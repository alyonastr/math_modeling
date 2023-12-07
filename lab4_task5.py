import numpy as np 
figure=input('Введите тип фигуры:')
a=input('Введите сторону/радиус')
b=input('Введите сторону/высоту')

def func(figure, a, b):
    if figure == 'круг':
        pl=3.14*(a**2)
    if figure == 'квадрат':
        pl=a*b
    if figure == 'треугольник':
        pl=(a*b)/2
    return pl

print(func(figure, a, b))