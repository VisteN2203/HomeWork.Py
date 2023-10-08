# объявление функции
import math


def is_valid_password(password, first_dot, second_dot):
	first_password = "".join(password[0:first_dot])
	second_password = "".join(password[first_dot + 1: second_dot])
	thread_password = "".join(password[second_dot + 1:])
	count = 0
	flag_second_pswd = True

	if first_password == first_password[::-1]:
		count += 1

	for i in range(2, int(second_password) // 2 + 1):
		if int(second_password) % i == 0:
			flag_second_pswd = False
			break

	if int(thread_password) % 2 == 0:
		count += 1

	if count == 2 and flag_second_pswd == True:
		return True
	else:
		return False


# считываем данные
psw = list(input())
if psw.count(":") == 2:
	first_double_dot = psw.index(":", 0)
	second_double_dot = psw.index(":", first_double_dot + 1)
	# вызываем функцию
	print(is_valid_password(psw, first_double_dot, second_double_dot))
else:
	print(0 > math.inf)


