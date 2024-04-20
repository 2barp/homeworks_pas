'''
# 1.
class CoffeeMachine:
    def __init__(self, water_level, coffee_level, milk_level, sugar_level=0, cups=0):
        self.water_level = water_level
        self.coffee_level = coffee_level
        self.milk_level = milk_level
        self.sugar_level = sugar_level
        self.cups = cups

    def add_water(self, amount):
        self.water_level+=amount

    def add_coffee(self, amount):
        self.coffee_level+=amount

    def add_milk(self, amount):
        self.milk_level+=amount

    def add_sugar(self, amount):
        self.sugar_level+=amount

    def add_cuos(self, number):
        self.cups+=number

    def check_resourses(self):
        if (self.water_level>0
                and self.coffee_level> 0
                and self.milk_level > 0
            and self.sugar_level > 0
            and self.cups > 0):
            return True
        else:
            return False


    def make_coffee(self):
        if self.check_resourses():
            self.water_level-=1
            self.coffee_level-=1
            self.milk_level-=1
            self.sugar_level-=1
            self.cups-=1
            print('Кофе готов!')
        else:
            print('Недостаточно ингредиентов')

cup_coffee = CoffeeMachine(1,5,3,2,4)
cup_coffee.make_coffee()
print(cup_coffee.check_resourses())
cup_coffee.make_coffee()
cup_coffee.make_coffee()

# 2.
class PhotoCamera:
    def __init__(self, brand, model, resolution, memory_capacity, photos, is_on=False):
        self. brand = brand
        self. model = model
        self.resolution = resolution
        self.is_on = is_on
        self.memory_capacity = memory_capacity
        self.photos = photos

    def take_photo(self):
        print(f'Сделана фотография с разрешением {self.resolution[0]}*{self.resolution[1]}')

    def get_camera_info(self):
        print(f'Марка: {self.brand}, Модель: {self.model}, Разрешение: {self.resolution[0]}*{self.resolution[1]}')

    def turn_on(self):
        self.is_on = True
        print('Фотокамера включена')

    def turn_off(self):
        self.is_on = False
        print('Фотокамера выключена')

    def is_camera_on(self):
        return self.is_on

    def store_photo(self, photo):
        if len(self.memory_capacity) > 0:
            self.photos.append(photo)
            self.memory_capacity-=1
            return True
        return False

    def view_photos(self):
        for photo in self.photos:
            print(f'Фотография №{(self.photos.index(photo))+1} с разрешением: {self.resolution[0]}*{self.resolution[1]}')

    def clear_memory(self):
        self.photos = []
        getattr(PhotoCamera, self.memory_capacity)

'''

# 3.
import random
class Revolver:
    def __init__(self):
        self.stock = 6
        self.storage = [None] * self.stock
        self.pointer = None

    def add_bullet(self, bullet):
        for slot in range(1, self.storage):
            if self.storage[slot] is None:
                self.storage[slot] = bullet
                return True
            else:
                return False

    def add_bullets_from_list(self, list):
        if len(self.storage) < 6:
            while len(self.storage) <= 6:
                for bullet in list:
                    self.storage.append(bullet)
            return True
        else:
            return False

    def shoot(self):
        if self.storage[self.pointer]!= None:
            self.storage.pop(self.pointer)
            if self.pointer<=5:
                self.pointer+=1
            else:
                self.pointer = 1
        else:
            return None

    def unload(self, all_items=False):
        if all_items==True:
            barrel = self.storage
            self.storage = [None] * self.stock
            return barrel
        else:
            if self.storage[self.pointer] is None:
                return None
            else:
                bullet = self.storage[self.pointer]
                self.storage[self.pointer] = None
                return bullet

    def scroll(self):
        self.pointer = random.randint(1,6)

    def bullet_count(self):
        return len(self.storage)

Revolver.add_bullet(bullet, bullet)
# comment
