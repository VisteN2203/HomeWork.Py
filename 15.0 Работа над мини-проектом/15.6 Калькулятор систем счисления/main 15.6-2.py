import math


def entering_the_correct_number():
	print("Введите число в шестнадцатеричной системе исчисления")
	while True:
		str_num = str(input())
		if str_num.isalnum() == True:
			total_str_num = 0
			for i in range(0, len(str_num)):
				if str_num[i] in "0123456789ABCDEF":
					total_str_num += 1
			if total_str_num == len(str_num):
				return str_num
			else:
				data_from_print = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
				print(f"Число в шестнадцатеричной системе исчисления может состоять только из этих символов- ")
				print(*data_from_print)
		else:
			print("Уберите спец символы из числа!")


def from_hexadecimal_to_decimal(str_num):
	list_str_num = []
	list_letter = ["A", "B", "C", "D", "E", "F"]
	for i in range(0, len(str_num)):
		if str_num[i] in "0123456789":
			list_str_num.append(int(str_num[i]))
		else:
			for j in range(0, len(list_letter)):
				if str_num[i] == list_letter[j]:
					list_str_num.append(10 + j)
				else:
					continue

	list_str_num.reverse()
	decimal_num = 0
	for n in range(0, len(list_str_num)):
		decimal_num += list_str_num[n] * math.pow(16, n)

	return int(decimal_num)


print("Привет! Это программа делает твое число из шестнадцатеричной системы исчисления в десятеричную")
str_num = entering_the_correct_number()
print(from_hexadecimal_to_decimal(str_num))
