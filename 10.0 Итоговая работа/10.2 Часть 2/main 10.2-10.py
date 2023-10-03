text = str(input())

findOneF = text.find("f", 0)
findTwoF = text.find("f", findOneF + 1)

if findOneF > -1 and findTwoF > -1:
	print(findTwoF)
elif findOneF == findTwoF == -1:
	print(findTwoF + findOneF)
else:
	print(findTwoF)