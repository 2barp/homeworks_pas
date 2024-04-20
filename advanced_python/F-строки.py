'''# 1.
for name in ['Александр','Алекс','Альберт']:
    for surname in ['Вотяк','Вотяков','Вотякович']:
        secondname = 'Романович'
        print(f'Диаплом с отличием вручается {surname}у {name}у {secondname}у')
# 2.
print(f'{input()}{int(input()):04}-{int(input()):03}')


# 3.
num1 = int(input())
num2 = int(input())
print(f'{num1:>9}\n{num2:>9}\n{num1+num2:>9}')


# 4.
amount = 100000000
r, k = int(input())/100,int(input())
for _ in range(k):
    amount += amount*r
print(f'{amount:,.2f}')


# 5.
for num1 in range(1,101):
    for num2 in range(1,101):
        res = num1 * num1
        if '0' in str(res):
            print(f'[DEBUG a={num1} b={num2} result={res}]')
'''

# 6.
