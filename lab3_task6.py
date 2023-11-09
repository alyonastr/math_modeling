import numpy as np 
N=6
M=5
a=np.zeros((N, M))
a[0,0]=55
a[0,1]=61
a[0,2]=4
a[0,3]=3
a[0,4]=5
a[1,0]=7
a[1,1]=8
a[1,2]=9
a[1,3]=11
a[1,4]=10
a[2,0]=13
a[2,1]=14
a[2,2]=15
a[2,3]=16
a[2,4]=8
a[3,0]=7
a[3,1]=6
a[3,2]=4
a[3,3]=7
a[3,4]=10
a[4,0]=11
a[4,1]=7
a[4,2]=8
a[4,3]=1
a[4,4]=2
a[5,0]=10
a[5,1]=5
a[5,2]=3
a[5,3]=4
a[5,4]=8

slice=a[0:2:1, 0:2:1]
print(slice)

slice=a[0:4:1, 0:1:1]
print(slice)

slice=a[0:1:1, 2::1]
print(slice)

slice=a[2:4:1, 1:3:1]
print(slice)

slice=a[1:3:1, 2:4:1]
print(slice)

slice=a[1:5:1, 2:5:1]
print(slice)

slice=a[4:6:1, 0:2:1]
print(slice)

slice=a[4:6:1, 2:5:1]
print(slice)