# 1.
def f(a, b):
    return 18 * a * b


print(f(1, 10))

# 2.
summa = 0
for i in range(1, 11):
    summa += i
print('The sum is: ', summa)


# 3.
def is_even(n):
    if n % 2 == 0:
        print(n, " is even")
    else:
        print(n, ' is odd')


is_even(4)


# 4.
def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(int(input())))


# 5.
def is_palindrome(s):
    s = s.lower()
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


print(is_palindrome(input()))


# 6.
def myltiplylist(list):
    if len(list) == 0:
        return None
    else:
        result = 1
        for i in range(len(list)):
            result *= list[i]
        return result

print(myltiplylist([int(input()) for x in range(int(input()))]))
