stringOne, stringTwo, stringThree = len(str(input())), len(str(input())), len(str(input()))

maximum = max(stringOne, stringTwo, stringThree)
minimum = min(stringOne, stringTwo, stringThree)
middle = (stringOne + stringTwo + stringThree) - (maximum + minimum)

if (maximum+minimum) - middle == middle:
    print("YES")
else:
    print("NO")