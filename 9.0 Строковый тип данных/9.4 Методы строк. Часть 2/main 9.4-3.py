num = int(input())

count = 0

for i in range(1, num + 1):
	string = str(input())
	if string.count("11") >= 3:
		count += 1
print(count)