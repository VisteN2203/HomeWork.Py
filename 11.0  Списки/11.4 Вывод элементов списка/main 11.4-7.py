num = int(input())
listMinus = []
listZero = []
listPlus = []

for i in range(num):
	nums = int(input())
	if nums < 0:
		listMinus.append(nums)
	elif nums == 0:
		listZero.append(nums)
	else:
		listPlus.append(nums)

list = listMinus + listZero + listPlus
print(*list, sep="\n")
