import math


def entering_the_correct_number():
	print("Введите число в двоичной системе исчисления")
	while True:
		str_num = str(input())
		if str_num.isdigit() == True:
			if str_num.count("1") + str_num.count("0") == len(str_num):
				num = int(str_num)
				return num
			else:
				print("Введите число состоящее только из 0 и 1")
				continue
		else:
			print("Введите число!")
			continue


def from_binary_to_decimal(binary_num):
	len_binary_num = len(str(binary_num))
	decimal_num = 0
	for i in range(0, len_binary_num):
		remains = binary_num % 10
		decimal_num += remains * math.pow(2, i)
		binary_num //= 10

	return int(decimal_num)


print("Привет! Это программа делает твое число из двоичной системы исчисления в десятеричную")
binary_num = entering_the_correct_number()
print(from_binary_to_decimal(binary_num))
