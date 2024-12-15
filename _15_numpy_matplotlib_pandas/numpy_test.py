import numpy as np

np.arcsin(1)
print("-----------numpy数组的算术运算------------")
# 将列表转换为数组
x = np.array([1.0, 2.00, 3.0],np.int32)  # 1-dimensional arrays with 3 elements
print(x)  # numpy默认打印会省去小数点后的0，会带一个点
print(type(x))
y=np.array([4,5,6,])
print(x+y)
print(x-y)
print(x*y)  # element-wise product
print(x/y)  # element-wise division
print(x/2)  # broadcasting

print("------------numpy生成数组------------")

print(np.ones(5))
print(np.zeros(5))
print(np.empty(5))
print(np.arange(0,12,1).reshape(3,4))  # 生成0-12的数组，步长为1，reshape成3*4的矩阵
a = np.random.random((2, 3))
print(a)
print(a.sum())
print(np.sum(a))
# the axis parameter indicates which axis gets collapsed.
# axis=0 collapses the rows (i.e., it sums the elements of each column),
print(np.sum(a, axis=0))
print(np.sum(a, axis=1))


print("------------矩阵的元素运算-------------")

# N-dimensional array
A = np.array([[1, 2, 3], [4, 5, 6, ]])
print(A)

print(type(A))
print(np.array([1, 2, 3]).shape)
print(A.shape)  # shape of the array
print(A.ndim)  # number of dimensions
print(A.dtype)  # data type
print(A.size)  # number of elements = torch中的x.numel()
B= np.array([[7,8,9], [-1,-2,-3]])
print(A+B)  # element-wise sum
print(A*B)  # element-wise product
print(A*10)  # broadcasting
print(x + A)  # broadcasting A是2*3的矩阵，x是1*3的矩阵，x会被扩展成2*3的矩阵
# 张量表示0,1,2,3,...,n维的数组

print("------------矩阵的矩阵运算-------------")
print(np.dot(A, B.T))  # matrix multiplication
print(A.dot(B.T))  # transpose and dot product

print("------------数组的合并与分割-------------")
print(A)
print(B)
print(np.vstack((A, B)))  # vertical stack 竖直方向加，变得是0维的
print(np.concatenate((A, B), axis=0))  # axis是什么，就保留什么维度
print(np.hstack((A, B)))  # horizontal stack 水平方向加，变得是1维的
print(np.concatenate((A, B), axis=1))
print(A[:, np.newaxis])  # add a new axis

print(np.vsplit(A,2))  # 竖直方向分割（从n*3变成1*3），变得是0维的。水平方向分割，则从3*n变成3*1
print(np.split(A,2,axis=0))  # split the array into 2 parts。axis=0 refers to the first axis (rows) in a 2D array.

print("------------数组的拷贝-------------")
C=A.copy()
A[0]=0
print(A)
print(C)


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









