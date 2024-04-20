# 6.
kvadrat = (x**2 for x in range(1,6))
print(next(kvadrat))
next(kvadrat)
print(next(kvadrat))
next(kvadrat)
print(next(kvadrat))

# 7.
suits = [' Пики',' Крести',' Червы',' Буби']
values = ['6','7','8','9','10','J','Q','K','A']
deck = ((value + suit) for suit in suits for value in values)
for card in deck:
    print(next(deck))