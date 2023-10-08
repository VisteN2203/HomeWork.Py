data = str(input())

listData = data.split(" ")

total = 0
for i in range(len(listData)):
	for j in range(i+1,len(listData)):
		if listData[i] == listData[j]:
			total += 1

print(total)