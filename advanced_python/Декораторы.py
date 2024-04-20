'''# 1.
import time
def timer(func):
    def inside_func(*args,**kwargs):
        start = time.time()
        work = func(*args,**kwargs)
        finish = time.time()
        print(f'{func.__name__} работала на протяжении {finish-start}')
        return work
    return inside_func



# 2.
def cache(func):
    dictionary = dict()
    def inside_function(arguments):
        if arguments not in dictionary:
            dictionary[arguments] = func(arguments)
        return dictionary[arguments]
    return inside_function
@cache
def f(x):
    if x <= 1:
        return 1
    else:
        return f(x - 1) + f(x - 2)


for i in range(100):
    print(i, f(i))
'''

# 3.

