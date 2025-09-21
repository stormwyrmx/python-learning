# import os
# os.fork() #只有linux系统支持

import multiprocessing,os,time

def worker1(name):
    print(f'{name}worker started,pid:{os.getpid()},ppid:{os.getppid()}')
    time.sleep(1)

def worker2(name):
    print(f'{name}worker started,pid:{os.getpid()},ppid:{os.getppid()}')
    time.sleep(1)

if __name__ == '__main__':
    print('主进程开始')
    processes=[]
    for i in range(5):
        p1 = multiprocessing.Process(target=worker1,args=('小琪琪',))
        p2 = multiprocessing.Process(target=worker2,args=('亚斯娜',))
        # start启动进程后会执行target中指向的函数的代码
        # 如果没有指定target参数，默认会执行Process类中的run方法
        p1.start()
        p2.start()
        # p1.terminate()
        # p2.terminate()
        print(p1.name,p1.is_alive())
        print(p2.name,p2.is_alive())

        processes.append(p1)
        processes.append(p2)


    for p in processes:
        # 阻塞当前进程/线程，直到调用join()方法的那个进程/线程执行完毕。
        # 并行执行是通过 start() 来开始的；join() 只是让调用方“等”，而不是让线程/进程“并行”。
        p.join()

    print('主进程结束')

