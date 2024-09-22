from _08_function import variable_test
from _08_function.atm_test import *

def function1():
    print("function1 starting!")
    num=1/0
    print("function1 finish!")

def function2():
    print("function2 starting!")
    function1()
    print("function2 finish!")

def fuck():
    try:
        function2()
    except Exception as e:
        print("出现异常了",e)
    finally:
        print(type([1,2]))

fuck()

