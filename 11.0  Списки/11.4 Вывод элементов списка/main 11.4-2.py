import math

num = int(input())
firstList = []

for i in range(num):
	nums = int(input())
	firstList.append(nums)

print(*firstList, sep="\n")
print()

secondList = []
for j in range(len(firstList)):
	f = math.pow(firstList[j], 2) + firstList[j] * 2 + 1
	secondList.append(int(f))

print(*secondList, sep="\n")
