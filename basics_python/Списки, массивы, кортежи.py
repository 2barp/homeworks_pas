# 3.
n=int(input())
mass, sum=[], 0
for i in range(n):
    num = int(input())
    mass.append(num)
    sum += num
print(sum/n)

# 4.
n,m = int(input()), int(input())
mass = []
for _ in range(n):
    number = int(input())
    mass.append(number)
print(mass[m])

# 5.
n, mass, sum = int(input()), [], 0
for _ in range(n):
    mass.append(int(input()))
for i in range(0, len(mass), 2):
    sum += mass[i]
print(sum)
