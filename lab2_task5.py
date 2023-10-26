a=int(input('Введите число:'))
b=int(input('Введите число:'))
d= a % b 
c= a//b
if b==0:
    print('На ноль делить нельзя')
else: 
    d=a%b
    c= a//b
    if d==0:
     print('Делится')
     print(c)
    else:
     print(d)
     print(c)