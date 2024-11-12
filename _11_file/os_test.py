import os

"""

"""

def os_functions():
    print(os.getcwd())
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
    print(os.stat("test_new.txt"))
    # 启动一个外部程序
    os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Anaconda3 (64-bit)/Anaconda Prompt.lnk")

def os_path_functions():
    print(os.path.abspath("test_new.txt"))
    print(os.path.exists("test_new.txt"))
    print(os.path.exists("girls"))
    print(os.path.join('../_15_numpy_matplotlib_pandas/', 'test_new.txt'))
    print(os.path.split('C:/Users/lenovo/Desktop/Python/Python-100-Days/Day01/test_new.txt'))  # 元组形式返回路径和文件名

    print(os.path.basename('C:/Users/lenovo/Desktop/Python/Python-100-Days/Day01/test_new.txt'))
    print(os.path.dirname('C:/Users/lenovo/Desktop/Python/Python-100-Days/Day01/test_new.txt'))
    print(os.path.isdir('girls'))
    print(os.path.isfile("test_new.txt"))



if __name__ == '__main__':
    # os_functions()
    # os_advanced_functions()
    os_path_functions()