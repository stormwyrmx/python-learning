class Phone:
    def __init__(self, producer,version):
        self.producer = producer
        self.version=version

    def call_by_4g(self):
        print("callling by 4g")

"""
继承的内容（通过super()调用）
属性：子类继承父类的所有属性。（继承的意思就是全部写进去）
方法：子类继承父类的所有方法。

需要重新写的内容
构造函数：如果子类需要初始化特定的属性，通常需要重写构造函数，并使用 super() 调用父类的构造函数。如果子类不重写构造函数，会自动调用父类的构造函数。
方法：如果子类需要不同的行为，可以重写父类的方法。
"""
class MyPhone(Phone):
    def __init__(self,producer,version,is_5g_available):
        super().__init__(producer,version)
        self.is_5g_available=is_5g_available

    def call_by_5g(self):
        if self.is_5g_available:
            print(self.producer)
            print("calling by 5g")
        else:
            super().call_by_4g()


phone1=MyPhone("Apple",14,False)
phone1.call_by_5g()
phone1.call_by_4g()
print(phone1.producer)
