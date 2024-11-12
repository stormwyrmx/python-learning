
def write_file():
    # 1.打开文件
    f = open('a.txt', 'w', encoding='utf-8')
    # 2.操作文件
    f.write('Hello, world!\n')
    # 3.关闭文件
    f.close()

def append_file():
    f = open('a.txt', 'a', encoding='utf-8')
    data=['姓名\t','年龄\t','性别\n','琪琪\t','18\t','女\n','麻衣\t','19\t','女\n']
    f.writelines(data)  # writelines接收一个字符串列表
    f.close()

def read_file():
    f = open('a.txt', 'r', encoding='utf-8')
    s = f.read()
    print(s,type(s))
    f.close()

def advance_read_file():
    f = open('b.txt', 'w+', encoding='utf-8')
    f.write("可爱的女孩子！\n")
    f.write("555，我想要女孩子了！")
    f.seek(3)  # 移动文件指针到第3个字节,utf-8编码中一个汉字占3个字节
    s = f.readlines()
    print(s,type(s))

def copy_file(src, dst):
    f1 = open(src, 'rb')  # binary mode doesn't take an encoding argument
    f2 = open(dst, 'wb')
    s = f1.read()
    f2.write(s)
    f2.close()
    f1.close()

if __name__ == '__main__':
    # write_file()
    # read_file()
    # append_file()
    # advance_read_file()
    copy_file('data/leishen.png', 'data/leishen_copy.png')