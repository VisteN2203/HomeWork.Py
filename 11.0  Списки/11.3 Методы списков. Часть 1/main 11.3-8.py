num = int(input())
list = []

for i in range(num):
	text = str(input())
	list.append(text)

numLetter = int(input())

for j in range(len(list)):
	string = list[j]
	lenString = len(string)
	if lenString >= numLetter:
		print(string[numLetter-1],end="")