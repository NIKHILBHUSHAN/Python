import time
import threading
def task():
    print("Child thread:",threading.current_thread().name)

t=threading.Thread(target=task)

t.start()

print("Main thread:",threading.current_thread().name)

t.join()
def task1():
    print("Task 1 satrted")
    time.sleep(3)
    print("Task 1 ended")
def task2():
    print("Task 2 started")
    time.sleep(3)
    print("Task 2 ended")
task1()
task2()
t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)
t1.start()
t2.start()
t1.join()
t2.join()
print("all task ccompleted")

def worker(num):
    print(f"Worker {num} started")
    time.sleep(2)
    print(f"Worker {num} completed")
threads=[]
for i in range(5):
    t=threading.Thread(target=worker,args=(i,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print("All workers completed")