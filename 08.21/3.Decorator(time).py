from time import time_ns,sleep,perf_counter

def func_duration(func):
    def wrapper(*args,**kwargs):
        t=time_ns()
        func(*args,**kwargs)
        print(f"функция отработала за {(time_ns()-t)/(10**9):.2f} сек")
    return wrapper

def func_duration_2(func):
    def wrapper(*args,**kwargs):
        t=perf_counter()
        func(*args,**kwargs)
        print(f"функция отработала за {perf_counter()-t} сек")
    return wrapper


@func_duration
@func_duration_2
def sleepy():
   sleep(1)

sleepy()