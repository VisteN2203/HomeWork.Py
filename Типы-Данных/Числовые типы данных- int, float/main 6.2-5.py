DogAge = int(input())

HumanAge1 = 10.5
HumanAge2 = 4

if DogAge == 1:
    print(HumanAge1)
else:
    DogAge = DogAge - 2
    HumanAge = (HumanAge2 * DogAge) + 21
    HumanAge = int(HumanAge)
    print(HumanAge)