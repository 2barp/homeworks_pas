'''# 1.
list = input()
dictionary = {}
for i in range(len(list)):
    dictionary[list[i]]=list[i]
print(dictionary)

# 2.
n = int(input())
dictionary = {}
for num in range(1, n + 1):
    dictionary[num] = num ** 2
print(dictionary)


# 3.
dictionary = {'data1':375, 'data2': 567, 'data3': -37, 'data4': 21}
proizv = 1
for i in dictionary.values():
    proizv*=i
print(proizv)


# 4.
string = input()
num=0
dictionary = {'.':num, ',':num, ':':num, ';':num, '!':num, '?':num}
punctuation = ['.',',',':',';','!','?']
for value in string:
    if value in punctuation:
        num = dictionary.get(value)
        dictionary[value]=num+1
print(dictionary)
'''

# 5.
string = input()
num = 0
mass = []
dictionary = {'0': num, '1': num, '2': num, '3': num, '4': num, '5': num, '6': num, '7': num, '8': num, '9': num}
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for value in string:
    if value in numbers:
        num = dictionary.get(value)
        dictionary[value] = num + 1
for k in dictionary.keys():
    if values >= 1:
        mass.append()
print(sorted(mass))
