"""
字符串工具类
"""

def str_reverse(s:str)->str:
    """
    字符串反转
    :param s:将要被反转的字符串
    :return:反转后的字符串
    """
    return s[::-1]

def substr(s:str,x:int,y:int)->str:
    """
    按照给定序号，对字符串进行切片
    :param s:即将被切片的字符串
    :param x:开始下标
    :param y:结束下标
    :return:切片完成后的字符串
    """
    return s[x:y]

if __name__ == '__main__':
    print(str_reverse("i love husiqi"))
    print(substr("i love husiqi",0,6))