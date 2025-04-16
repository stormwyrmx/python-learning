import os

"""
The os module in Python provides a way of 
using operating system-dependent functionality
"""

def os_functions():
    print(os.getcwd())  # cwd=current working directory
    print(os.listdir())  # list all files in the current directory
    print(os.listdir("../data"))  # list all files in the data directory
    # os.mkdir("girls")
    # os.makedirs("girls/pretty")
    # os.rmdir("girls/pretty")
    # os.removedirs("/girls/pretty")
    os.chdir("../data")  # change the current directory，程序路径发生了改变
    print(os.getcwd())  # cwd=current working directory
    print("--------walk--------")
    for dirs,dirlist,filelist in os.walk("../_15_numpy_matplotlib_pandas"):
        print(dirs)
        print(dirlist)
        print(filelist)


def os_advanced_functions():
    # with open("test.txt","w") as f:
    #     f.write("hello world")
    # os.remove("test.txt")
    # os.rename("test.txt","test_new.txt")

    # 获取文件的属性
    print(os.stat("data/test_new.txt"))
    # 启动一个外部程序
    os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Anaconda3 (64-bit)/Anaconda Prompt.lnk")

def os_path_functions():
    os.path.abspath(__file__)
    print(os.path.abspath("data/test_new.txt"))
    print(os.path.exists("data/test_new.txt"))
    print(os.path.exists("girls"))
    print(os.path.join('../_15_numpy_matplotlib_pandas/', 'test_new.txt'))
    print(os.path.split('C:/Users/lenovo/Desktop/Python/Python-100-Days/Day01/test_new.txt'))  # 元组形式返回路径和文件名

    print(os.path.basename('C:/Users/lenovo/Desktop/Python/Python-100-Days/Day01/test_new.txt'))
    print(os.path.dirname('C:/Users/lenovo/Desktop/Python/Python-100-Days/Day01/test_new.txt'))
    print(os.path.isdir('girls'))
    print(os.path.isfile("data/test_new.txt"))



if __name__ == '__main__':
    choice=input('please insert 1 to 3\n')
    if choice == '1':
        os_functions()
    elif choice == '2':
        os_advanced_functions()
    elif choice == '3':
        os_path_functions()
    else:
        print("无效选择")
