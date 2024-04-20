# 2.
mass = [int(input()) for num in range(int(input()))]
print(list(map(lambda val: val**3, mass)))

# 3.
mass = [int(input()) for num in range(int(input()))]
print(list(filter(lambda num: num<0, mass)))

# 4.
from functools import reduce
num = int(input())
mass = [(x-1) for x in range(2,num+2)]
print(reduce(lambda num1,num2: num1*num2, mass))

# 5.
from functools import reduce

mass = [int(input()) for num in range(int(input()))]
kratnie = list(filter(lambda x: (x ** 2) % 9 == 0, mass))
print(reduce(lambda val1,val2: val1 if val1>val2 else val2, kratnie))

