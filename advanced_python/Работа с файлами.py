with open('', 'r') as file:
    string1 = file.read() # 1
    string2 = file.readline() # 2
    string3 = file.readlines() # 3
    string4 = string1.split('\n') # 4
    for line in file: # 5
        print(line, end='\n')
    string6 = ' '.join(file.readlines()).replace('\n','') # 6
    mass_of_strs = file.readlines() # 7
    for lines in mass_of_strs:
        lines.replace(' ','')
        lines.replace('\n', '')
        lines.replace('\t', '')
        print(lines)
