from time import time_ns, sleep, perf_counter


def func_duration(func):
    def wrapper(*args, **kwargs):
        start = time_ns()
        func(*args, **kwargs)
        print(f"функция отработала за {(time_ns() - start)/10**9:.2f} сек")
    return wrapper

def func_duration_2(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        print(f"функция отработала за {perf_counter() - start} сек")
    return wrapper


@func_duration
@func_duration_2
def sleepy():
    sleep(1)

sleepy()