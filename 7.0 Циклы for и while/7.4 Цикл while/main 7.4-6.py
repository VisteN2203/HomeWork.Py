number = int(input())

numberOfFives = 0

while 1 <= number <= 5:
    if number == 5:
        numberOfFives += 1
        number = int(input())
    else:
        number = int(input())


print(numberOfFives)