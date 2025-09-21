import subprocess

# Run a simple command
def run_command():
    # subprocess.run()在接收命令字符串作为参数时，不会自动分割命令和参数。当你传入'ls -a'作为单个字符串时，它会将整个字符串作为程序名称来查找，而不是将其解析为命令和参数。
    # subprocess.run('ls -a')
    # subprocess.run('ls')
    # subprocess.run(['ip', 'addr'])

    # shell=True：系统会使用 shell（在 Windows 上是 cmd.exe，在 Unix 上是 /bin/sh）来解释和执行该命令
    subprocess.run('cat data/output.txt | grep data', shell=True)

def run_error_command():
    # check=True：如果命令执行失败（退出码非0），抛出 subprocess.CalledProcessError 异常
    p1 = subprocess.run(['ls', '-a'], capture_output=True,text=True,check=True)
    print(p1)
    print(p1.returncode)

def run_command2file():
    # 将输出重定向到文件
    with open('data/output.txt', 'w') as f:
        subprocess.run(['ls', '-a'], stdout=f, text=True)

if __name__ == '__main__':
    choice = input("请选择要运行的功能：1-run_command，2-run_error_command，3-run_command2file\n")
    if choice == '1':
        run_command()
    elif choice == '2':
        run_error_command()
    elif choice == '3':
        run_command2file()
    else:
        print("无效选择")
