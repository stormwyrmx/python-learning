def with_write_file():
    with open('data/src.txt', 'w',encoding='utf-8') as f:  # /src.txt是绝对路径，是根目录下的。或者也可以写为./src.txt
        f.write('你好，世界！\n')

def with_read_file():
    with open('data/src.txt', 'r',encoding='utf-8') as f:
        s = f.read()
        print(s)

def with_copy_file(src,dst):
    with open(src,'r',encoding='utf-8') as file1:
        with open(dst,'w',encoding='utf-8') as file2:
            file2.write(file1.read())

if __name__ == '__main__':
    with_write_file()
    with_read_file()
    with_copy_file('data/src.txt','data/dst.txt')
