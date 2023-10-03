num = int(input())
list = []
listNumber = []

for i in range(0, num):
	numbers = int(input())
	listNumber.append(numbers)

for i in range(0, num - 1):
	sum = listNumber[i] + listNumber[i + 1]
	list.append(sum)

print(list)