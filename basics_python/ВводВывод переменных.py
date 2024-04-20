# 1; Программирование после школы!
string1 = input()
string2 = input()
string3 = input()
print(string1 + string2 + string3)

# 2; 32134205104895.5
from math import sqrt

a, b = int(input()), int(input())
exp = 2 ** 8 * a ** 8 - 2 ** 4 * a ** 4 + 2 ** 2 * a ** 2 - 2 * b + 0.5 * sqrt(b) + ((a * b) ** (b + a)) / 2
print(exp)

# 5; 2325
num = int(input())
print(num - 1, num + 1, sep='')

# 6; 1234
kilometrs = int(input())
print(kilometrs//10**5)