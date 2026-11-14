import time
import multiprocessing
import os
def calculate():
    result=0
    for i in range(10_000_000):
        result+=i
    return result
start=time.time()
calculate()
calculate()
end=time.time()
print("time taken:",end-start)
def square(n):
    print(f"Square of {n}",n*n)
def task();
    print("child process ID:",os.getpid())
    print("Parent process ID",os.getppid())

if __name__=="__main__":
    p1=multiprocessing.Process(target=calculate)
    p2=multiprocessing.Process(target=calculate)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("All Process completed")

    p1=multiprocessing.Process(target=square,args=(5,))
    p2=multiprocessing.Process(target=square,args=(10,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("Main process ID:",os.getpid())

    p=multiprocessing.Process(target=task)
    p.start()
    p.join()    

