string = str(input())

list = string.split()

for i in range(len(list)):
	word = list[i]
	word += word[0]
	word += "ки"
	list[i] = word[1:]

print(*list)