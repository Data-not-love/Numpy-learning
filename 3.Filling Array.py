import numpy as np

a = np.full((2,3,3),9)
print (a) # in ra mảng 2 3X4 và fill 9

b = np.zeros((10,2,2))# khởi tạo giá trị 0
print (b) # in mảng với giá trị mặc định 0

c = np.ones((10,2,2))
print (c)

d = np.empty((5,5,5))# hàm empty không khởi tạo giá trị mà cấp phát bộ nhớ
print (d)

e = np.arange(0,1001,5) #bắt đầu, kết thúc, bước
print(e)

f = np.linspace(0,1000,2)#bắt đầu, kết thúc, số lượng giá trị muốn in