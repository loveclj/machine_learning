#encoding=utf-8
import numpy as np
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print a.shape
print a
a.shape =(4,3)
print a.shape
print a

print np.logspace(0,2,10)

string ="abcdef"

print np.fromstring(string, np.int8)
print np.fromstring(string, np.int16)

def func(i):
    return i%2

print np.fromfunction(func, (10,))

def sqr(i,j):
    return i*i + j*j

print np.fromfunction(sqr, (9,9))

a = np.arange(10)
print a
print a[:-1]
print a[::-1]
print a[5:1:-2]

x = np.arange(10)
print x
y = x[[1,1,2,4,4]]
print y

x = np.arange(5,0,-1)
print x

a = np.random.rand(10) # 产生一个长度为10,元素值为0-1的随机数的数组
print a

print a > 0.5

print a[a > 0.5]

a = np.arange(20)
a = np.array(a)
print a
a.shape = (4,5)
print a

print a[0,:]
print a[1:3,2:4]
print a[(1,2,3),(0,1,2)] #用于存取数组的下标和仍然是一个有两个元素的组元,组元中的每个元素都是整数序列,分别对应数组的第0轴和第1轴。从两个序列的对应位置取出两个整数组成下

##########np struct
persontype  = np.dtype({'names':['name', 'age','weight'], 'formats':['S32','i', 'f']})

a = np.array([("zhang", 32, 75.3),("li",9,20.1)], dtype=persontype)
print a
print a.dtype
a[0]["name"] = "chen"
print a

