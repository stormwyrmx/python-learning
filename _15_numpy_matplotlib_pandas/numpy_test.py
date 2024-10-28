import numpy as np


np.arcsin(1)
print("-----------numpy数组的算术运算------------")
x = np.array([1.0, 2.00, 3.0])  # 1-dimensional arrays with 3 elements
print(x)  # numpy默认打印会省去小数点后的0
print(type(x))
y=np.array([4,5,6,])
print(x+y)
print(x-y)
print(x*y)  # element-wise product
print(x/y)  # element-wise division
print(x/2)  # broadcasting

print("------------矩阵的算数运算-------------")

# N-dimensional array
A = np.array([[1, 2, 3], [4, 5, 6, ]])
print(A)
print(A.shape)  # shape of the array
print(A.ndim)  # number of dimensions
print(A.dtype)  # data type
B= np.array([[7,8,9], [-1,-2,-3]])
print(A+B)  # element-wise sum
print(A*B)  # element-wise product
print(A*10)  # broadcasting
print(x + A)  # broadcasting A是2*3的矩阵，x是1*3的矩阵，x会被扩展成2*3的矩阵
# 张量表示0,1,2,3,...,n维的数组

print("------------访问元素-------------")
print(type(A))
for i in A:
    for j in i:
        print(j)
# 使用数组访问各个元素
A=A.flatten()
print(A)
print(type(A))
print(A[np.array([0, 2, 4])])  # 这是 NumPy 数组的高级索引功能，允许你使用数组作为索引来访问特定位置的元素。
print(A>3)  # 这是 NumPy 数组的广播和元素级比较操作，返回一个布尔数组，表示每个元素是否满足条件。
print(A[A>3])  # 这是布尔索引，使用布尔数组来选择满足条件的元素。











