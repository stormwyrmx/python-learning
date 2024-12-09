class Phone:
    def __init__(self, producer,version):
        self.producer = producer
        self.version=version

    def call_by_4g(self):
        print("callling by 4g")

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