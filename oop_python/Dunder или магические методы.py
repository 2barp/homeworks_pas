'''# 1.
def infiltrate():
    pass

signature = "-~=$([{PETR}])$=~-"

class SignedMessage:

    def __new__(cls, *args, **kwargs):
        infiltrate()
        return object.__new__(cls)

    def __init__(self, message, signature):
        self.message = message
        self.signature = signature

    def __str__(self):
        return f'{self.message} {self.signature}'

    def __add__(self, other):
        return SignedMessage(self.message + other.message, self.signature)

print(SignedMessage("Hello ", signature))
print(SignedMessage("world!", signature))
print(SignedMessage("Hello ", signature) + SignedMessage("world!", signature))


# 2.
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return Vector2(- self.x, - self.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return '{' + f'{self.x},{self.y}' + '}'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y

    def __mul__(self, other):
        return sum(self.x * other.x, self.y * other.y)


class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y, self.z + other.z)

    def __neg__(self):
        return Vector2(- self.x, - self.y, - self.z)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y, self.z - other.z)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __str__(self):
        return '{' + f'{self.x},{self.y},{self.z}' + '}'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y and self.z != other.z

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z'''

# 3.
class Item:
    def __init__(self, ID, price, rarity, color):
        self.ID = ID
        self.price = price
        self.rarity = rarity
        self.color = color

    def __lt__(self, other):
        if self.ID < other.ID:
            return True
        if self.ID > other.ID:
            return False
        if self.price < other.price:
            return True
        if self.price > other.price:
            return False
        if self.rarity > other.rarity:
            return True
        if self.rarity < other.rarity:
            return False
        if oct(self.color) > oct(other.color):
            return True
        if oct(self.color) < oct(other.color):
            return False

    def __le__(self, other):
        pass


