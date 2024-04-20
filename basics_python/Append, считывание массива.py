# 1.
n, m, mass = int(input()), int(input()), []
mass.append(n)
mass.append(m)
print(mass, n + m, sep=' ')

# 2.
mass = []
for i in input().split(' '):
    mass.append(i)
print(mass[0], mass[-1])

# 3.
mass, max_len, string = [], 0, ''
for _ in input().split(' '):
    mass.append(_)
for i in range(len(mass)):
    if len(mass[i])> max_len:
        max_len=len(mass[i])
        string = mass[i]
print(string)

# 4.
n, mass = int(input()), []
for i in range(1,n+1):
    if i%3==0 or i%5==0:
        mass.append(i)
print(sum(mass))

# 5.
mass, counter, answer = [], 0, ''
for i in input().split(' '):
    mass.append(i)
for k in range(len(mass)):
    if mass.count(mass[k]) > counter:
        counter = mass.count(mass[k])
        answer = mass[k]
print(answer)


