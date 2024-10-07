import numpy as np
d = {'1':'A'}
a = np.array([[1,2,3],
              [4,"Hello World",6],
              [7,8,9]])

print (a.dtype) # in ra kiểu dữ liệu là string dưới 11 ký tự
print (a[0]) # in ký tự trong list 0
print (a[1,0:2]) # in 2 chuỗi đầu trong list 2
print (a[0][0]) # in ra số 1
print (type(a[0][0])) # in chuỗi str
print (type(a[1,0:2])) # in 2 chuỗi đầu trong list 2 kiểu ndarray

b = np.array([[1,2,3],
              [4,d,6],
              [7,8,9]])

print (b.dtype)
print (b[1,1])

c = np.array([[1,2,3],
              [4,d,6],
              [7,8,"Hello"]])

print (c.dtype)


d = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]], dtype="<U7")
print (d.dtype)