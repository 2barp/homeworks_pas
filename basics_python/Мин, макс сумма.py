# 1.
n = int(input())
for i in range(n):
    if i % 3 == 0 and i % 6 != 0:
        print(i)

# 2.
n = int(input())
for i in range(10, n):
    if i % 2 == 0:
        print(i)

# 3.
n, counter, sum = int(input()), 0, 0
if n % 2 == 0:
    for i in range(1, n + 1):
        if i % 2 == 0:
            counter += 1
    print(counter)
else:
    for i in range(1, n + 1):
        if i % 2 != 0:
            sum += i
    print(sum)

# 4.
n, counter, string = int(input()), 0, ''
if n % 3 == 0:
    m = int(input())
    for i in range(1, n):
        if i % m == 0:
            counter += 1
    print(counter)
else:
    for i in range(1, n):
        print(n ** i, end=' ')

# 5.
a, b, n, counter = int(input()), int(input()), int(input()), 0
legs = (a ** 2) + (b ** 2)
for _ in range(n):
    hypotenyse = int(input())
    if (hypotenyse ** 2 == legs) and ((hypotenyse % 3 == 0) or (hypotenyse % 4 == 0)):
        counter += 1
print(counter)
