import multiprocessing,os,time


class MyProcess(multiprocessing.Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f'{self.name}worker started,pid:{os.getpid()},ppid:{os.getppid()}')

if __name__ == '__main__':
    print('主进程开始执行')
    processes = []
    for i in range(5):
        p = MyProcess(f'worker{i}')
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print('主进程结束执行')