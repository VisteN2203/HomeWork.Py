# объявление функции
def is_password_good(password):
	count = 0
	text_length = len(password)
	if text_length >= 8:
		count += 1
	else:
		return count

	for capital_letter in range(len(password)):
		if 90 >= ord(password[capital_letter]) >= 65:
			count += 1
			break

	for lowercase_letter in range(len(password)):
		if 122 >= ord(password[lowercase_letter]) >= 97:
			count += 1
			break

	for number in range(len(password)):
		if 57 >= ord(password[number]) >= 48:
			count += 1
			break

	return count

def is_true_or_false(count):
	if count == 4:
		flag = True
	else:
		flag = False

	return flag

# считываем данные
txt = input()

# вызываем функцию
count = is_password_good(txt)
print(is_true_or_false(count))
