string = str(input())

listOne = list(string.split())
listTwo = []

for i in listOne:
	listTwo.append(int(i))


minList = min(listTwo)
maxList = max(listTwo)

positionMin = listTwo.index(minList)
positionMax = listTwo.index(maxList)

listTwo[positionMin] = maxList
listTwo[positionMax] = minList

print(*listTwo)

