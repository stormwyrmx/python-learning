class Phone:
    __is_5g_enable=True

    def __init__(self,__is_5g_enable):
        self.__is_5g_enable=__is_5g_enable

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5G is enabled")
        else:
            print("5G is disabled,use 4G")

    def call_by_5g(self):
        self.__check_5g()
        print("the phone is calling")

phone1=Phone(False)
phone1.call_by_5g()