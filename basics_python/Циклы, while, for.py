# 1;
x = int(input())
while (x%2!=0 and x%10!=5):
    x=int(input())

# 2;
for i in range(10):
    print(i)

# 3;
k, n = int(input()), int(input())
sum = 0
while k <= n:
    if k % 2 != 0:
        sum += k
    k += 1
print(sum)

# 4;
n = int(input())
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)
