'''# 2.
import copy, sys
mass = []
for i in range(5):
    mass.append(int(input()))
mass1 = mass[:]
mass2 = mass.copy()
mass3 = copy.copy(mass)
mass4 = copy.deepcopy(mass)
mass5 = list(mass)
print(sum(mass))

# 4.
import sys
animals = ['cat', 'cat', 'dog', 'dog', 'bird', 'capybara', 'capybara', 'capybara']
dictionary = {}
num = 1
for animal in animals:
    if animal not in dictionary.keys():
        dictionary[animal] = num
    else:
        num = dictionary.get(animal)
        dictionary[animal] = num + 1
print(sys.getrefcount('cat')+sys.getrefcount('dog')+sys.getrefcount('bird')+sys.getrefcount('capybara'))
print(sys.getrefcount(1)+sys.getrefcount(2)+sys.getrefcount(3))

# 5.
ssulka, ravni = 0, 0
string, mass = '', []
backpack= ['capybara', 'capyraba', 'capyba', 'capyba', 'capybara', 2999, 2999, 'capybara', [7,7,7], [7,7,7], [7,7,7]]
backpack += [[8,8]]*5
for num1 in range(len(backpack)):
    for num2 in range(len(backpack)):
        string+=str(num1)
        string+=str(num2)
        mass.append(string)
        string = ''
print(mass)
        if num1 is num2:
            if string==str(list(string)[:]):
                ssulka+=1
        if num1==num2:
            ravni+=1
print(ssulka,ravni)'''

# 6.
caesar = ['lettuce', 'chicken', 'cheese', 'sauce', 'tomatoes', 'croutons']
caesar.append(caesar)

