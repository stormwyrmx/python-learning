import numpy as np

"""
w:权重
b:偏转
theta:阈值
"""


def and_gate(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


def and_gate_v2(x1, x2):
    """
    在NumPy中，np.array 和 np.sum 是通过 NumPy 模块导入的对象。
    尽管 np.sum 是一个函数，许多 IDE 会将它标记为 v，因为它实际上是一个对象的引用。
    NumPy 中的许多函数和常量都可能被实现为内置对象，因此IDE可能将它们识别为 v。
    """
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def nand_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def or_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([1, 1])
    b = -0.7
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def xor_gate(x1, x2):
    s1 = nand_gate(x1, x2)
    s2 = or_gate(x1, x2)
    y = and_gate_v2(s1, s2)
    return y
