people = int(input())

people = -people
berth = 4
coupe = 9

place = (people // berth)

place = (place**2) ** 0.5

print(int(place))