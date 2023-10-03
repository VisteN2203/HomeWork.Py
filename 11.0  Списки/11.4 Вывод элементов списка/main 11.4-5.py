num = int(input())
list = []

for i in range(num):
	list.append(str(input()))

searchList = []
search = str(input())
for i in range(len(list)):
	string = list[i]
	if search.lower() in string.lower():
		searchList.append(string)
print(*searchList,sep="\n")
