a=int(input('Введите a:'))
b=int(input('Введите b:'))
c=int(input('Введите c:'))
D=(b**2)-(4*(a*c))
if D<0:
    print('Нет корней')
else:
    if D==0:
     x=-b/(2*a)
     print(x) 
     if  D>0:
      k=(-b-D**0.5)/(2*a)
      m=(-b+D**0.5)/(2*a)
     print(k)
     print(m)