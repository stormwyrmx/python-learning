# import def_test

def fuck():
    # 函数的声明和定义放在一起了，这里的girl相当于java中的重新定义一个变量叫girl。如果要用外面的girl，则要定义global全局变量
    global girl
    girl = "xiaoqiqi"
    print(id(girl))
    # global boy="kilitoku"
    # The global keyword is used to declare that a variable inside a function is global,
    # but it should not be assigned a value in the same statement.

def greet():
    print("hello, "+name)


if __name__ == '__main__':

    age: int = 18
    girl: str = "husiqi"
    fuck()
    name='sakura' # 在调用函数之前，如果函数内部使用的是全局变量，就要先定义好
    greet()
    # name='sakura'
    print(id(girl))
    print(age)



