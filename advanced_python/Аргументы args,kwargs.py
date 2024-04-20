# 1.
def sum_numbers(*numbers):
    summ= 0
    for number in numbers:
        summ+=number
    return summ

print(sum_numbers(10,20,30,40))

# 2.
def print_kwargs(**arguments):
    for value in arguments:
        print(f'{value}: {arguments[value]}')

print_kwargs(name = 'Alice', age = 25, country = 'usa')

# 3.
def filter_by_lenght(min_lehght, *strings):
    answer = []
    for string in strings:
        if len(string) >= min_lehght:
            answer.append(string)
    return answer

values = ['hello','world', 'how', 'are', 'you']

print(filter_by_lenght(4, *values))


# 4.
def calculate_total_price(price, **prices):
    total_price = price
    for coupon, value in prices.items():
        total_price = total_price - (total_price*value) // 100
    return total_price


print(calculate_total_price(200, holiday=25))
print(calculate_total_price(100, student=10, coupon=20))


# 5.
def custom_print(*args, **kwargs):
    separator = kwargs.get('sep', ' ')
    end_of_answer = kwargs.get('end', '\n')
    if end_of_answer!='\n':
        end_of_answer+='\n'
    mass = []
    for argument in args:
        mass.append(str(argument))

    for value, key in kwargs.items():
        if value!='sep' and value!='end':
            mass.append(f'{value}={key}')

    print(separator.join(mass), end=end_of_answer)


custom_print(1, 2, 3, a=4, b=5, sep='-', end='!')
custom_print(a=1,b=2,sep = '  ')
