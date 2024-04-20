'''# 1.
from abc import  ABC, abstractmethod
class Book:
    def __init__(self, title, author):
        self.title = title
        self. author = author

    @abstractmethod
    def display(self):
        pass

class Autobiography(Book):
    def display(self):
        print(f'"{self.title}" - прекрасная книга, написанная в автобиографическом жанре. Автор - {self.author}')

class Psychology(Book):
    def display(self):
        print(f'"{self.title}" - прекрасная книга, написанная в жанре психологии. Автор - {self.author}')


class Fantasy(Book):
    def display(self):
        print(f'"{self.title}" - прекрасная книга, написанная в жанре фантастики. Автор - {self.author}')

book1 = Autobiography('К черту все! Берись и делай!', 'Ричард Брэнсон')
book2 = Psychology('Биология добра и зла', 'Роберт Сапольски')
book3 = Fantasy('Песнь льда и пламени', 'Джордж Реймонд Ричард Мартин')

book1.display()
book2.display()
book3.display()
'''

# 3.
from abc import abstractmethod
class Human:
    def __init__(self, name):
        self. name = name

    @abstractmethod
    def answer_question(self):
        print('Очень интересный вопрос! Давайте разбираться вместе!')


class Student(Human):
    def ask_question(self, someone, question):
        self.someone = someone
        self.question = question
        print(f'{self.someone}, {self.question}?')
        someone.answer_question(question)

