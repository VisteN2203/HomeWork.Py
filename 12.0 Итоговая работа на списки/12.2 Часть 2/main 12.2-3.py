list = str(input()).split()

total = 0
for i in range(len(list)):
	total += int(list[i])

print("+".join(list), "=", total, sep="")
