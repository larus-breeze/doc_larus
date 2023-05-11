# Just a helper to convert a txt listing to a python list

filename = 'f50.txt'
elementList = []

with open(filename) as file:
    for line in file.readlines():
        elementList.append(line.rstrip('\n'))

print(elementList)
