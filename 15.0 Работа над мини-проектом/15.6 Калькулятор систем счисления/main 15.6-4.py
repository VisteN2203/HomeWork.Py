def entering_the_correct_number():
	print("Введите число в десятичной системе исчисления исчисления")
	while True:
		str_num = str(input())
		if str_num.isdigit() == True:
			return int(str_num)
		else:
			print("Введите только числа!")
			continue


def from_decimal_to_binary(decimal_num):
	list_binary = []
	while decimal_num != 0:
		remain = decimal_num % 2
		list_binary.append(remain)
		decimal_num //= 2

	list_binary.reverse()
	str_binary = ""
	for i in range(0, len(list_binary)):
		str_binary += str(list_binary[i])

	return str_binary


print("Привет! Это программа делает твое число из десятеричной системы исчисления в двоичную")
decimal_num = entering_the_correct_number()
print(from_decimal_to_binary(decimal_num))
