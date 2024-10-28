# import def_test

girl:str="husiqi"
age:int=18

def fuck():
    # 函数的声明和定义放在一起了，这里的girl相当于java中的重新定义一个变量叫girl。如果要用外面的girl，则要定义global全局变量
    global girl
    girl = "xiaoqiqi"
    # global boy="kilitoku"
    # The global keyword is used to declare that a variable inside a function is global,
    # but it should not be assigned a value in the same statement.



if __name__ == '__main__':
    fuck()

print(girl)
print(age)


