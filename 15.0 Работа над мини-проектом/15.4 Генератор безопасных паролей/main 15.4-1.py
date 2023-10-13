import random


def start():
	print("Привет! Это программа генерирует заданное количество паролей и включает в себя умную настройку на длину \n"
		  "пароля, а также на то, какие символы требуется в него включить, а какие исключить.")


def count_of_passwords():
	print("Введите количество паролей(Числом)")
	num_of_passwords = int(input())
	return num_of_passwords


def password_length(password_number):
	print(f"Введите {password_number} длину пароля(Числом)")
	len_password = int(input())
	return len_password


def is_numbers():
	while True:
		print("Включать ли цифры 0123456789?; д = да, н = нет")
		response = str(input())
		if response == "д":
			flag_is_number = True
			return flag_is_number
		elif response == "н":
			flag_is_number = False
			return flag_is_number
		else:
			continue


def is_uppercase_letters():
	while True:
		print("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?; д = да, н = нет")
		response = str(input())
		if response == "д":
			flag_is_uppercase_letters = True
			return flag_is_uppercase_letters
		elif response == "н":
			flag_is_uppercase_letters = False
			return flag_is_uppercase_letters
		else:
			continue


def is_lowercase_letters():
	while True:
		print("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?; д = да, н = нет")
		response = str(input())
		if response == "д":
			flag_is_lowercase_letters = True
			return flag_is_lowercase_letters
		elif response == "н":
			flag_is_lowercase_letters = False
			return flag_is_lowercase_letters
		else:
			continue


def is_special_characters():
	while True:
		print("Включать ли спец. символы !#$%&*+-=?@^_?; д = да, н = нет")
		response = str(input())
		if response == "д":
			flag_is_special_characters = True
			return flag_is_special_characters
		elif response == "н":
			flag_is_special_characters = False
			return flag_is_special_characters
		else:
			continue


def is_ambiguous_characters():
	while True:
		print("Исключать ли неоднозначные символы il1Lo0O; д = да, н = нет")
		response = str(input())

		if response == "д":
			flag_is_ambiguous_characters = True
			return flag_is_ambiguous_characters

		elif response == "н":
			flag_is_ambiguous_characters = False
			return flag_is_ambiguous_characters

		else:
			continue


def data_generation():
	list = []

	if flag_is_number == True:
		list.append([48, 57])

	if flag_is_uppercase_letters == True:
		list.append([65, 90])

	if flag_is_lowercase_letters == True:
		list.append([97, 122])

	if flag_is_special_characters == True:
		list.append([[33, 47], [58, 64], [91, 96], [123, 126]])

	return list


chars = ""
bad_characters = [105, 108, 49, 76, 111, 48, 79]
start()
list_password = []
num_of_passwords = count_of_passwords()

for i in range(1, num_of_passwords + 1):
	len_password = password_length(i)
	flag_is_number = is_numbers()
	flag_is_uppercase_letters = is_uppercase_letters()
	flag_is_lowercase_letters = is_lowercase_letters()
	flag_is_special_characters = is_special_characters()
	flag_is_ambiguous_characters = is_ambiguous_characters()
	list = data_generation()

	for j in range(0, len_password):
		rnd_num_len_list = random.randrange(0, len(list))
		len_list_in_list = len(list[rnd_num_len_list])

		if len_list_in_list == 2:
			get_first_num = list[rnd_num_len_list][0]
			get_second_num = list[rnd_num_len_list][1]

			while flag_is_ambiguous_characters == True:
				forming_random_numb_from_the_range = random.randrange(get_first_num, get_second_num + 1)
				if forming_random_numb_from_the_range in bad_characters:
					continue
				else:
					break
			else:
				forming_random_numb_from_the_range = random.randrange(get_first_num, get_second_num + 1)
			chars += chr(forming_random_numb_from_the_range)

		if len_list_in_list == 4:
			get_rnd_num_list_in_list = random.randrange(0, len_list_in_list)
			get_first_num = list[rnd_num_len_list][get_rnd_num_list_in_list][0]
			get_second_num = list[rnd_num_len_list][get_rnd_num_list_in_list][1]

			while flag_is_ambiguous_characters == True:
				forming_random_numb_from_the_range = random.randrange(get_first_num, get_second_num + 1)
				if forming_random_numb_from_the_range in bad_characters:
					continue

				else:
					break

			else:
				forming_random_numb_from_the_range = random.randrange(get_first_num, get_second_num + 1)

			chars += chr(forming_random_numb_from_the_range)

	list_password.append(chars)
	chars = ""

for n in range(0, len(list_password)):
	print(f"{n + 1} номер вашего пароля.\n"
		  f"Пароль под номером {n + 1} - {list_password[n]}")
