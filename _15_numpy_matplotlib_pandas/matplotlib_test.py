import matplotlib.pyplot as plt
import numpy as np
# from numpy import *
# import matplotlib

"""
文档字符串
matplotlib是用于绘制图形和实现可视化的库。它提供了一种类似于MATLAB的方式来绘制图形。
绘图工具：matplotlib、seaborn
"""

def draw_sin():
    x=np.arange(0, 2*np.pi, 0.01)
    y1=np.sin(x)
    y2=np.cos(x)
    plt.plot(x,y1,label='sin')
    plt.plot(x,y2,label='cos',linestyle='--')
    plt.legend()
    plt.show()

def read_image():
    n1 = plt.imread('kumiko.png')  # 底层会调用matplotlib.image.imread
    # plt.imshow(n1)
    n2 = np.array([0.299, 0.587, 0.114])
    result = np.dot(n1, n2)
    plt.imshow(result, cmap='gray')
    plt.show()

draw_sin()
read_image()



