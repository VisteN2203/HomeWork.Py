num = int(input())
list = []

for _ in range(num):
	list.append(str(input()))

numTwo = int(input())
listTwo = []

for _ in range(numTwo):
	listTwo.append(str(input()))

total = 0
for i in range(num):
	stringCheck = list[i]
	for j in range(numTwo):
		stringFind = listTwo[j]
		if stringFind.lower() in stringCheck.lower():
			total += 1
			if total == numTwo:
				print(stringCheck, sep="\n")
	total = 0