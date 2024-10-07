import numpy as np
arr = np.array([[2,34,5],
                [1,78,1],
                [7,8,98]])
print (np.sort(arr)) # sắp xếp giá trị từ bé -> lớn cho từng list
print (np.sort(arr,axis=0)) # sắp xếp giá trị từ bé đến lớn của cột 0,1,2
print(np.sort(arr,kind='merge',)) # sắp xếp giá trị từ bé -> lớn cho từng list và chọn thuật toán sắp xếp
ar1 = np.array([[2,34,78],
                [4,5,7],
                [78,67,9]])
print (np.sort(ar1,kind='heapsort'))


print (np.concatenate((arr,ar1), axis=0, out=None, dtype=None))
arr2 = np.array([[2,3,45,4],[45,334,3,3]])
print (arr2)
print (arr2.reshape(4,2))

print (np.reshape(arr2, newshape=(4,2), order='C'))


def area_rectangle (height= 0, witdh= 0):
    return height*witdh

print (area_rectangle())