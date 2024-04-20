'''# 1.
def calculate_answer(mass):
    try:
        mass = mass.split(' ')
        num1,num2 = float(mass[0]), float(mass[2])
        print(num1/num2)
    except ZeroDivisionError:
        print('ERROR')

calculate_answer(input())

# 2.
def find_password(*passwords):
    can_be_password = []
    for password in passwords:
        try:
            int(password,16)
            can_be_password.append(password)
        except ValueError:
            print(f'Пароль {password} не подходит')
    print(f'Эти пароли могут подойти: {can_be_password}')

find_password('djvhkjfkj', '6788326379273', '8377389/')

# 3.
olympiad1 = {"name": "Пробная вышка",
             "winners": {
                 "Олеся Олимпиадникова": 594,
                 "Олег Олимпиадников": 587,
                 "Онисим Олимпиадников": 581,
             }
             }
olympiad2 = {"name" : "Горные воробьи",
    "winners": {
        "Ольга Олимпиадникова": (20, 20, 19, 20) ,
        "Олеся Олимпиадникова": (19, 19, 20, 20, 17),
        "Офелия Олимпиадникова": (20, 20, 20, 20, 13)
    }
             }

def check_winner(name):
    try:
        results_olympiad1 = olympiad1['winners'][name]
        status = 'победитель'
        print(f'[{olympiad1["name"]}] {status} {results_olympiad1}')
    except KeyError:
        status = 'призёр'
        print(f'[{olympiad1["name"]}] {status}')
    finally:
        print('--'*10)

    try:
        results_olympiad2 = olympiad2['winners'][name][4]
        status='победитель'
        print(f'[{olympiad2["name"]}] {status} {results_olympiad2}')
    except KeyError:
        status = 'призёр'
        print(f'[{olympiad2["name"]}] {status}')
    except IndexError:
        status = 'победитель'
        print(f'[{olympiad2["name"]}] {status} Баллы за задачу не найдены')
    finally:
        print('--'*10)

check_winner('Ольга Олимпиадникова')
check_winner('Олеся Олимпиадникова')


# 4.
def ugly_function():
    try:
        while True:
            pass
    except KeyboardInterrupt:
        ugly_function()

"""ugly_function()"""
'''

# 5.
print('Заходит однажды тестировщик в бар и заказывает...')
mug = input()
try:
    if int(mug) == 0:
