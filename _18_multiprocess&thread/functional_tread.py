import threading,os,time


def thread_function():
    time.sleep(1)
    print("Thread %s: starting" % threading.current_thread().name)

if __name__ == '__main__':
    threads=[threading.Thread(target=thread_function) for i in range(10)]

    for thread in threads:
        thread.start()
        # thread.join()

    print("Main    : all done")
