import numpy as np

l1 = [1,2,3]
l2 = [4,5,6]

a1 = np.array(l1)
a2 = np.array(l2)

print (l1*5) # l1 * vô hướng 5
print (a1*5) # nhân các giá trị vs 5
print (a2+5)
print (l1+l2) # gộp 2 list lại một
print (a1+a2) # cộng tương ứng 2 phần tử trong list

a3 = np.array([1,2,3]) # 1X3
a4 = np.array([
              [1],
              [2]]) # 2X1

print (a3+a4)

a5 = np.array([[1,2,3],[4,5,6]])
print (np.sqrt(a5))