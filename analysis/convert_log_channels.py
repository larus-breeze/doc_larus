filename = 'f120format.txt'
elementList = []

with open(filename) as file:
    for line in file.readlines():
        elementList.append(line.rstrip('\n'))

print(elementList)
