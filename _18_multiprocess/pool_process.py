import time,os
from multiprocessing import Pool

def task(name):
    print(f'{name} started,pid:{os.getpid()},ppid:{os.getppid()}')
    time.sleep(1)

# 非阻塞式
def async_run():
    start_time = time.time()
    print('主进程开始')
    # 创建一个进程池，最大进程数为3
    pool = Pool(3)
    for i in range(10):
        pool.apply_async(task, args=(f'任务{i}',))
    pool.close()
    pool.join()
    print('主进程结束')

# 阻塞式
def sync_run():
    start_time = time.time()
    print('主进程开始')
    # 创建一个进程池，最大进程数为3
    pool = Pool(processes=3)
    for i in range(10):
        pool.apply(task, args=(f'任务{i}',))
    pool.close()
    pool.join()
    print(f'主进程结束,用时{time.time()-start_time}秒')

if __name__ == '__main__':
    # async_run()
    sync_run()