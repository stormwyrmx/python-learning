import numpy as np
import matplotlib.pyplot as plt

n1 = plt.imread('kumiko.png')
# plt.imshow(n1)
n2 = np.array([0.299, 0.587, 0.114])
result = np.dot(n1, n2)
plt.imshow(result, cmap='gray')

plt.show()
plt.rcParams