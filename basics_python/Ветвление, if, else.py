# 2;
password_first, password_second = input(), input()
print(password_first == password_second)

# 3;
num1, num2, num3, num4 = int(input()), int(input()), int(input()), int(input())
min_num = 0
if num1 < num2:
    min_num = num1
else:
    min_num = num2
if num2 < num3:
    min_num = num2
else:
    min_num = num3
if num3 < num4:
    min_num = num3
else:
    min_num = num4
print(min_num)

# 4;
num1, num2, num3, num4 = int(input()), int(input()), int(input()), int(input())
max_num = 0
if num1 > num2:
    max_num = num1
else:
    max_num = num2
if num2 > num3:
    max_num = num2
else:
    max_num = num3
if num3 > num4:
    max_num = num3
else:
    max_num = num4
print(max_num)

# 5;
side1, side2, side3 = int(input()), int(input()), int(input())
if side1 > side2:
    max_side = side1
elif side2 > side3:
    max_side = side2
else:
    max_side = side3
other_side = (side1 + side2 + side3) - max_side
print(max_side < other_side)

# 6;
side1, side2, side3 = int(input()), int(input()), int(input())
if side1 == side2 == side3:
    print('Треугольник равносторонний')
if side1 + side2 == side3 or side1 + side3 == side2 and side2 + side3 == side1:
    print('Треугольник вырожденный')
else:
    print('Треугольник разносторонний')
# 7;
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if b < c and d < a:
    print(0)
if a < d and c < b:
    print(b - c + 1)
elif c < b and a < d:
    print(d - a + 1)
elif a == c and b == d:
    print(b - a + 1)
elif a < d and b == c:
    print(1)
elif c < b and a == d:
    print(1)
