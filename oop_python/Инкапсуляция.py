# 1.
from random import *


class CRM:
    def __init__(self):
        self.__abiturients = {}

    def add(self, abiturient):
        # получение СНИЛСа
        number = abiturient.get_number()

        # добавление абитуриента в словарь,
        # где информация хранится под СНИЛСами
        self.__abiturients[number] = abiturient

    def get_status(self, number):
        return self.__abiturients[number].__check()


class Abiturient:
    def __init__(self, name, surname, patronymic, age, number, bvi=False):
        self.__name = name
        self.__surname = surname
        self.__patronymic = patronymic
        self.__age = age
        # СНИЛС
        self.__number = number
        # Russian National Exam (ЕГЭ), баллы
        self.__RNE = self.__fetch_RNE()
        # есть ли БВИ
        self.__bvi = bvi

    @property
    def get_number(self):
        return self.__number

    @property
    def get_surname(self):
        return self.__surname

    @get_surname.setter
    def get_surname(self, surname):
        self.__surname = surname

    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def get_name(self, name):
        self.__name = name

    @property
    def get_patronymics(self):
        return self.__patronymic

    @get_patronymics.setter
    def get_patronymics(self, patronymic):
        self.__patronymic = patronymic

    @property
    def get_age(self):
        return self.__age

    @get_age.setter
    def get_age(self, age):
        self.__age = age

    @property
    def rne(self):
        return self.__RNE

    @rne.setter
    def rne(self, RNE):
        self.__RNE = RNE

    @property
    def get_bvi(self):
        return self.__bvi

    @get_bvi.setter
    def get_bvi(self, bvi):
        self.__bvi = bvi

    # функция получения результатов ЕГЭ
    def __fetch_RNE(self):
        return tuple(randint(0, 100) for _ in range(3))

    # функция ответа на вопрос, проходит ли абитуриент
    def __check(self):
        if self.__bvi:
            return "Да"
        if random() > 0.95:
            return "Да"
        return "Нет"


module = CRM()

# добавление АР-а в список абитуриентов
module.add(Abiturient("Александр", "Вотяков", "Романович", 18, "111-222-333 00", True))

# добавление РА в список абитуриентов
module.add(Abiturient("Роман", "Вотяков", "Александрович", 18, "333-222-111 00"))

# проверка, проходят ли абитуриенты
print(module.get_status("111-222-333 00"))
print(module.get_status("333-222-111 00"))
