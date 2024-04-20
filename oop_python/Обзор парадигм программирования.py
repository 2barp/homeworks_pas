# 1.

# объектно ориентированное программированиеё
class NumberList:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum_of_squares(self):
        result = 0
        for num in self.numbers:
            result += num ** 2
        return result

numbers = [1, 2, 3, 4, 5]
number_list = NumberList(numbers)
total = number_list.sum_of_squares()
print(f"Sum of squares: {total}")

# функциональное программирование
def sum_of_squares(numbers):
    squared_nums = map(lambda x: x ** 2, numbers)
    return sum(squared_nums)

numbers = [1, 2, 3, 4, 5]
total = sum_of_squares(numbers)
print(f"Sum of squares: {total}")

# императивное программирование
def sum_of_squares(numbers):
    result = 0
    for num in numbers:
        result += num ** 2
    return result

numbers = [1, 2, 3, 4, 5]
total = sum_of_squares(numbers)
print(f"Sum of squares: {total}")

# 2.
def sum_even_numbers(numbers):
    result = sum([x for x in numbers if x%2==0])
    return result

print(sum_even_numbers([14, 93, 19, 38, 18, 51, 77]))

# 3.
def sum_even_numbers(numbers):
    summ = 0
    for num in numbers:
        if num%2==0:
            summ+=num
    return summ

print(sum_even_numbers([60, 84, 9, 49, 7, 85, 38]))