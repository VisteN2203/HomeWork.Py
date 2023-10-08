numberAndSharp = str(input())
number = int(numberAndSharp[1:])

list = []
for i in range(number):
	newText = str(input())
	findSharp = newText.find("#")
	if findSharp > -1:
		newTextWithoutSharp = newText[0:findSharp]
		list.append(newTextWithoutSharp.rstrip())
	else:
		list.append(newText)

print(*list, sep="\n")
