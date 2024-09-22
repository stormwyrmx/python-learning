def hello():
    print("hello _08_function!")

if __name__ == '__main__':
    hello()


def covid_19(temperature):
    """
    判断体温是否正常
    :param temperature:体温
    :return:None
    """
    if temperature<=37.5:
        print("体温正常")
    else:
        print("发烧")


# covid_19(float(input("请输入体温：")))
