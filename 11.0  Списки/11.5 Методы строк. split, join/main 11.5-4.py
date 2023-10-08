nums = str(input())
number = nums.split(" ")

for i in range(len(number)):
	print("+" * int(number[i]))