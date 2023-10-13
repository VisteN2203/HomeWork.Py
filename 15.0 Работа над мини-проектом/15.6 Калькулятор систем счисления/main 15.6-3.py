import math


def entering_the_correct_number():
	print("Введите число в десятичной системе исчисления исчисления")
	while True:
		str_num = str(input())
		if str_num.isdigit() == True:
			return int(str_num)
		else:
			print("Введите только числа!")
			continue


def from_decimal_to_hexadecimal(decimal_num):
	list_decimal = []
	while decimal_num != 0:
		remain = decimal_num % 16
		list_decimal.append(remain)
		decimal_num //= 16

	list_decimal.reverse()

	str_hexadecimal_num = ""
	list_letter = ["A", "B", "C", "D", "E", "F"]
	for i in range(0, len(list_decimal)):
		if str(list_decimal[i]) in "0123456789":
			str_hexadecimal_num += str(list_decimal[i])
		else:
			for j in range(0, len(list_letter)):
				if list_decimal[i] == 10 + j:
					str_hexadecimal_num += list_letter[j]
					break
				else:
					continue

	return str_hexadecimal_num


print("Привет! Это программа делает твое число из десятеричной системы исчисления в шестнадцатеричную")
decimal_num = entering_the_correct_number()
print(from_decimal_to_hexadecimal(decimal_num))
