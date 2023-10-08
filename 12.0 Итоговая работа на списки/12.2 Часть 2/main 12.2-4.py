string = str(input())

list = [string[i] for i in range(len(string))]

total = 0
totalList = -1

if len(list) == 14:
	if list[0] == "7":
		total += 1
		totalList = len(list)
		if (list[1] and list[5] and list[9]) == "-":
			total += 3
			del list[1], list[4], list[7]
			for i in range(1, len(list)):
				if list[i] in "0123456789":
					total += 1

elif len(list) == 12:
	totalList = len(list)
	if (list[3] and list[7]) == "-":
		total += 2
		del list[3], list[6]
		for i in range(len(list)):
			if list[i] in "0123456789":
				total += 1

if totalList == total:
	print("YES")
else:
	print("NO")
