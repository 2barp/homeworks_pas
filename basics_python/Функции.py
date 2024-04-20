'''# 1.
def summation(mass):
    summ = 0
    for _ in range(len(mass)):
        summ+=mass[_]
    return summ

mass = [int(input()) for x in range(8)]
print(summation(mass))

# 2.
def checker(diapason):
    num = int(input())
    if num>=diapason[0] or num<=diapason[-1]:
        return True
    return False

diapason = [int(input()) for x in range(2)]
print(checker(diapason))

# 4.
def palindrom(num):
    number=list(num)
    if number==number[::-1]:
        return True
    return False

print(palindrom(input()))

# 5.
def checker_simple(num):
    if num==0 or num==1:
        return False
    for divider in range(2,int((num)**0.5)+1):
        if num%divider==0:
            return False
    return True

print(checker_simple(int(input())))

# 6.
def fibonacchi(num):
    if num==1:
        return 0
    if num==2 or num==3:
        return 1
    return fibonacchi(num-1)+fibonacchi(num-2)

print(fibonacchi(10))'''

# 3.
def is_perfect(num):
    sum_del=[]
    if num>0:
        for x in range(1,int((num)**0.5)+1):
            if num%x==0:
                sum_del.append(x)
        if num == (sum(sum_del)):
            return True
    return False

print(is_perfect(6))
