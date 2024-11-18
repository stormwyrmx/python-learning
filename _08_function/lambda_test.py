"""
将lambda函数赋值给一个变量，通过这个变量间接调用该lambda函数(do not assign a lambda expression, use a def)
或者作为内联函数：在需要一个简单函数的地方使用，例如 map()、filter() 和 sorted() 等函数。
"""

x = lambda a, b: a + b

print(x(5, 6))

m = list(map(lambda a: a ** 2, [1, 2, 3, 4, 5]))
print(m)