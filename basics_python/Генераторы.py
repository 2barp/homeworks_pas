# 1.
print(sum(x ** 2 for x in range(1, 101)))

# 3.
print(len([x for x in range(1, 21) if x % 2 == 0]))

# 4.
print(len([int(x) for x in input().split() if int(x) % 2 == 0][::2]))

# 5.
print(len([x for x in range(1, 1001) if x % 7 == 0 or x % 11 == 0]))
