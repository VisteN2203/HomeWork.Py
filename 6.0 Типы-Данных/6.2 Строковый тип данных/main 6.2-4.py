CityOne, CityTwo, CityThree = str(input()), str(input()), str(input())

CityOneNumber = len(CityOne)
CityTwoNumber = len(CityTwo)
CityThreeNumber = len(CityThree)

maximum = max(CityOneNumber, CityTwoNumber, CityThreeNumber)
minimum = min(CityOneNumber, CityTwoNumber, CityThreeNumber)

if minimum == CityOneNumber:
    print(CityOne)
    if maximum == CityTwoNumber:
        print(CityTwo)
    else:
        print(CityThree)
elif minimum == CityTwoNumber:
    print(CityTwo)
    if maximum == CityOneNumber:
        print(CityOne)
    else:
        print(CityThree)
else:
    print(CityThree)
    if maximum == CityOneNumber:
        print(CityOne)
    else:
        print(CityTwo)