# 1.
string = ''
for x in range(1,11):
    for y in range(1,11):
        string += str(x * y) + " "
        if y==10:
            string += '\n'
print(string)

# 2.
l, r, counter = int(input()), int(input()), 0
for x in range(l,r+1):
    for y in range(l, r + 1):
        for k in range(l, r + 1):
            if (x**2 + y**2) == k**2:
                counter+=1
print(counter)

# 3.
n = int(input())
dividers_a = []
dividers_b = []
for a in range(1, int(n / 2) + 1):
    if n % a == 0:
        dividers_a.append(a)
for b in range(1, int(n / 2) + 1):
    if n % b == 0:
        dividers_b.append(b)
for a in range(0,n):
    for b in range(0,n):
        if a == sum(dividers_b) and b==sum(dividers_a):
            print(a,b)

# 4.
n, string = int(input()), ''
for a in range(0, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0, 10):
                string += str(a) + str(b) + str(c) + str(d)
                if a ** n + b ** n + c ** n + d ** n == int(string):
                    if int(string)!= 0 and int(string)!= 1:
                        print(int(string))
                string = ''
