text = str(input())

list = []

for i in range(len(text.split())):
	string = text.split()
	LenSting = len(string[i])
	list += [LenSting]

print(max(list))