import matplotlib

class Girl:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def print_self(self):
        print(f"姓名:{self.name},年龄:{self.age},地址:{self.address}")

    def say_hello(self):
        print(f"Hello, I'm {self.name}, {self.age} years old.")

for i in range(1,4):
    print(f"当前录入第{i}位女孩子的信息,总共需要录入3位女孩子")
    girl=Girl(input("请输入姓名:"),input("请输入年龄:"),input("请输入地址:"))
    girl.print_self()


