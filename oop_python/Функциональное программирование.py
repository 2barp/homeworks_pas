# 1.
def factorial(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

# 2.
def is_prime(n):
    list_of_nums= [x for x in range(1, int(n**0.5)+1)]
    return all(n&i!=0 for i in (list_of_nums))

print(is_prime(4))
print(is_prime(7))

# 3.
def filter_od(numbers):
    func = lambda num: num%2!=0
    return list(filter(func,numbers))

print(filter_od([17,28,26,24,10,3256,49,6,12]))

# 4.
def map_sqaure(numbers):
    kvadrator =lambda num: num**2
    return list(map(kvadrator, numbers))

print(map_sqaure([1,2,3,4,5,6]))

# 5.
from functools import reduce


def reduce_sum(numbers):
    return reduce(lambda num1, num2: num1 + num2, numbers)


print(reduce_sum([1, 2, 3, 4, 5, 6]))

# 6.
def partial_apply(func, num1):
    def partical_func(num2):
        return func(num1, num2)
    return partical_func



# 7.
def compose(f,g):
    def h(argument):
        result1 = f(argument)
        return g(result1)
    return h

# 8.
def create_function_with_arguments(func,arguments):
    def new_func():
        return func(arguments)
    return new_func

# 9.
def compose_functions(functions):
    def composed_function(argument, index=0):
        if index>=len(functions):
            return argument
        new_argument = functions[index](argument)
        index+=1
        return composed_function(new_argument, index)
    return composed_function

