import numpy as np
#
# a = np.array([1,2,3,4])
# print (a)
# print (type (a))
# print (a[0:3])
# print (a[-2:])
#
# a[2] = 10
# print (a)
#
# #numpy có thể dùng mảng nhiều chiều
#
# a_mul = np.array([[1,2,3],
#                   [4,5,6],
#                   [7,8,9]])
#
# b_mul = np.array([[1,2,3,4],
#                   [5,6,7,8],
#                   [10,11,12,13],
#                   [14,15,16,17]])
# print(a_mul[1])# lấy all giá trị list 1
# print(a_mul[2,2])# lấy giá trị index 2 của list 2
# print (a_mul.shape)# đưa ra cấp của ma trận
# print ("Chieu : " + str (a_mul.ndim))
# print ("Size : " + str (a_mul.size))
# print (b_mul.shape)
#
# c_mul = np.array([[[1,2,3],
#                    [1,2,3],
#                    [1,2,3]],
#                   [[1,1,1],
#                   [1,1,1],
#                   [1,1,1]]])
#
# print (c_mul.shape)# in ra 2 ma trận có kích thước 3x3
# print ("Chieu : " + str(c_mul.ndim))
# print ("Size : " + str(c_mul.size))
# print ((c_mul.dtype))


d = np.array([1,1,11,2])
print(d[:3]) # in ra index 0 đến 2
print(d[2:4])
print(d[:]) # in all giá trị trong mảng
print(d[-1:]) # nếu in truy cập từ phần tử cuối thì index là -1
print(d[::-1]) # In ngược mảng thì slicing vs bước -1
print(d[0:4:3])

arr = np.array([[1,2,3],
                [5,6,4],
                [9,1,5]]) # LIST IN LIST OR NESTED LIST

print (arr)
print (arr[0:2]) # slicing : chỉ định vùng truy cập, in ra mảng 2 chiều chứa 1 hàng đầu
print (arr[0]) # indexing : truy cập giá trị theo index, in mảng 1 chiều vì chỉ lấy 1 hàng
print (arr.ndim) # 2
print (arr.shape) #
print (arr.shape == arr.ndim)
print (arr.size) # Arrays are typically “homogeneous”( đồng nhất ), meaning that they contain elements of only one “data type”
print (arr.data) # chỉ địa chỉ ô nhớ

print (np.zeros(5)) # ma trận 1x5
print (np.zeros((2,2))) # 1 ma trận 2x2
print (np.zeros((2,2,2))) # 2 ma trận 2x2

print (np.empty(4))
print (np.empty((2,3)))
print (np.empty((4,2,1)))

print (np.arange(0,10,3))
print (np.arange(-100,2,1))
print (np.arange(10))

print(np.linspace(2,3,1000))
print (arr.dtype) # int32
print (type(arr)) # trả về đối tượng ndarray