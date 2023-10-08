data = str(input())

data = data.split(".")

total = 0
for i in range(len(data)):
	if 255 >= int(data[i]) >= 0:
		total += 1

if total == 4:
	print("ДА")
else:
	print("НЕТ")