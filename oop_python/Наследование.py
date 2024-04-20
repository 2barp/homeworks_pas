# 1.
class HeavenlyBody:
    'Родительский класс HeavenlyBody'
    def __init__(self, name, age, temperature, radius):
        self.name = name
        self.age = age
        self.temperature = temperature
        self.radius = radius

    def display(self):
        return print(
            f'Название: {self.name}, Возраст: {self.age}, '
            f'Температура: {self.temperature}, Радиус: {self.radius}'
        )

class Planet(HeavenlyBody):
    'Дочерний класс Planet'

    def __init__(self, name, age, temperature, radius, orbital_speed):
        super().__init__(name, age, temperature, radius)
        self.orbital_speed = orbital_speed

    def display(self):
        super().display()
        print(f'Орбиталная скорость: {self.orbital_speed}')


class Star(HeavenlyBody):
    'Дочерний класс Star'

    def __init__(self, name, age, temperature, radius, constellation):
        super().__init__(name, age, temperature, radius)
        self.constellation = constellation

    def display(self):
        super().display()
        print(f'Создвезие: {self.constellation}')

planet1 = Planet('Земля', 4540, '16.92', 6371, '29.8')
star1 = Star('Полярная звезда', 60, '5500', 47, 'Малая Медведица')

print(Planet.__doc__, end='\n')
planet1.display()

print(Star.__doc__, end='\n')
star1.display()

# 2.
import random
import datetime
from datetime import date
class Pastry:
    def __init__(self, name, price, manufacture_date, term):
        self.name = name
        self.price = price
        self. manufacture_date = manufacture_date
        self.term = term

    def display(self):
        return print(f'Наименование: {self.name}, Цена: {self.price}, Дата изготовления: {self.manufacture_date}, Срок хранения: {self.term}')

    def valid_until(self):
        data = str(date.today())
        today = date.fromisoformat(data)
        date_until = abs(today - date.fromisoformat(str(self.manufacture_date)))
        return date_until.days

class Cake(Pastry):
    def __init__(self, name, price, manufacture_date, term, filling):
        super().__init__(name, price, manufacture_date, term)
        self.filling = filling

    def order(self):
        if self.valid_until() >=1:
            return f'Название: {self.name},\n Цена: {self.price},\nДата изготовления: {self.manufacture_date},\n Начинка: {self.filling}\n ,' \
               f'Срок годности истекает через: {self.valid_until()}\n , Оформлен заказ {random.randint(1,10**6)} - Торт с начинкой {self.filling}'
        else:
            return 'Не можем оформить Ваш заказ, пожалуйста, выдерите другую позицию'

class BentoCake(Pastry):
    def __init__(self, name, price, manufacture_date, term, celebration):
        super().__init__(name, price, manufacture_date, term)
        self.celebration = celebration

    def order(self):
        if self.valid_until() >= 1:
            return f'Название: {self.name},\n Цена: {self.price},\nДата изготовления: {self.manufacture_date},\n Праздник: {self.celebration}\n ,' \
                   f'Срок годности истекает через: {self.valid_until()},\n Оформлен заказ {random.randint(1, 10 ** 6)} - Бенто торт на {self.celebration}'
        else:
            return 'Не можем оформить Ваш заказ, пожалуйста, выдерите другую позицию'

cake1 = Cake('Торт', 1300, datetime.date(2023, 7, 20), 3, 'вишня')
bento1 = BentoCake('Бенто торт', 1000, datetime.date(2023, 7, 20), 4, 'день рождения')

cake1.order()
bento1.order()


# 3.
class BankAccount:
    def __init__(self, holder, balance, interest_rate):
        self.__holder = holder
        self._balance = balance
        self._interest_rate = interest_rate

    @property
    def get_holder(self):
        return self.__holder

    @get_holder.setter
    def get_holder(self, holder):
        self.__holder = holder

    def __str__(self):
        print(f'Владелец: {self.__holder}\n'
              f'Баланс: {self._balance}\n'
              f'Процентная ставка: {self._interest_rate}')

class BankOperation(BankAccount):
    def __init__(self, holder, balance, interest_rate):
        super().__init__(holder, balance, interest_rate)
        self.self_id = id(self)
        self.transaction = []

    def deposit(self,amount):
        self._balance += amount
        self.transaction.append(f'Пользователь {self.self_id} внес {amount} на счет')

    def withdraw(self, amount):
        self._balance -= amount
        self.transaction.append(f'Пользователь {self.self_id} снял {amount} со счета')

    def add_interest(self):
        self._balance *= (1+self._interest_rate)
        self.transaction.append(f'На счет клиента {self.self_id} начислились проценты. Сумма: {self._balance}')

    def history(self):
        for transaction in self.transaction:
            print(transaction)

account = BankOperation('Warren Buffett', 113000000000, 0.08)

account.__str__()
account.deposit(4000000000)
account.withdraw(88000000000)
account.add_interest()
account.history()


# 5.
class Investments:
    def __init__(self, ticker, price, currency, industry):
        self.ticker = ticker
        self.price = price
        self.currency = currency
        self.industry = industry

    def display(self):
        print (f'Тикер: {self.ticker},\n'
               f'Цена: {self.price},\n'
               f'Валюта: {self.currency},\n'
               f'Сектор: {self.industry}')


def byuing_secuities(func):
    def function(argument):
        if argument.echelon == 3:
            print (f'Это высокорискованная сделка')
            return None
        return func(argument)
    return function

class Shares(Investments):
    def __init__(self, ticker, price, currency, industry, dividend, echelon, profit):
        super().__init__(ticker, price, currency, industry)
        self.dividend = dividend
        self.echelon = echelon
        self. profit = profit

    @byuing_secuities
    def buying(self):
        if self.profit > 5:
            value = int(input())
            print(f'Количество: {value}')
            print(f'Совершена покупка акций на {self.price * value} рублей.')
        else:
            print('Сделка может быть неудачной, не стоит вкладываться в эту акцию!')


class Bonds(Investments):
    def __init__(self, ticker, price, currency, industry, coupon, echelon, nominal):
        super().__init__(ticker, price, currency, industry)
        self. coupon = coupon
        self.echelon = echelon
        self.nominal = nominal
    @byuing_secuities
    def buying(self):
        if self.price <= self.nominal:
            value = int(input())
            print(f'Количество: {value}')
            print(f'Совершена покупка облигаций на {self.price*value} рублей ')
        else:
            print('Сделка может быть неудачной, не стоит вкладываться в эту облигацию!')


i1 = Shares('GAZP', 174, 'RUB', 'Энергетика', True, 1, 6)
i1.display()
i1.buying()
i2 = Bonds('ОФЗ-26233', 688, 'RUB', 'Государственные', 6, 1, 1000)
i2.display()
i2.buying()

