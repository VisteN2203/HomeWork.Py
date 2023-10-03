list = []
UniCode = 97

for i in range(1, 27):
	inList = (chr(UniCode) * i)
	list.append(inList)
	UniCode += 1

print(list)
