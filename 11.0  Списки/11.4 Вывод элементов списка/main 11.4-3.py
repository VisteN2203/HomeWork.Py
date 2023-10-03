num = int(input())
list = []

for i in range(num):
	nums = int(input())
	list.append(nums)

maxNum = 0
minNum = 0
for i in range(len(list)):
	if list[i] == max(list):
		maxNum = i
	elif list[i] == min(list):
		minNum = i

del list[maxNum]
if minNum >= len(list):
	del list[minNum-1]
else:
	del list[minNum]

print(*list, sep="\n")
