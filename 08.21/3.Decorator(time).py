from time import time_ns, sleep, perf_counter


def func_duration(func):
    def wrapper(*args, **kwargs):
        start = time_ns()
        func(*args, **kwargs)
        print(f"функция 1 отработала за {(time_ns() - start)/10**9} сек")
    return wrapper

def func_duration_2(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        print(f"функция 2 отработала за {perf_counter() - start} сек")
    return wrapper


# КОММЕНТАРИЙ: несколько декораторов применямых к одной функции вкладываются друг в друга и выполняются в порядке перечисления в обратном порядке от заголовка функции
#ok
@func_duration
@func_duration_2
def sleepy():
    sleep(1)

sleepy()

# stdout:
# функция 2 отработала за 0.9999502999999095 сек
# функция 1 отработала за 1.0002048 сек


# ИТОГ: верно — 6/6
