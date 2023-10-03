import math

num = int(input())
list = []

for i in range(num):
	numInList = int(input())
	numInList = math.pow(numInList,3)
	list.append(int(numInList))
print(list)
