"""
__all__ is a list in a Python module that defines the public interface of the module.
It specifies which names should be imported when from module import * is used.
If __all__ is not defined, the import * statement will import all names that do not start with an underscore (_).
改变的是命令空间，但是默认还是先把所有内容都执行一遍
"""
# __all__=['count_girl','print_girl']
__all__=['print_girl']

import sys

count=0

def print_girl(name):
    print(name)

def count_girl():
    print(count)
    print(sys.path)
    print("package:", __package__)

count_girl()

"""
如果当前模块是主模块，__name__的值是__main__，并执行下列代码
"""
if __name__ == '__main__':
    count_girl()


