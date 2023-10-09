# Название Проекта - "Угадайка чисел"

# Описание проекта:
# программа генерирует случайное число в диапазоне от 1 до 100 и просит пользователя угадать это число.
# Если догадка пользователя больше случайного числа, то программа должна вывести сообщение
# 'Слишком много, попробуйте еще раз'. Если догадка меньше случайного числа, то программа должна вывести сообщение
# 'Слишком мало, попробуйте еще раз'. Если пользователь угадывает число, то программа должна поздравить его и
# вывести сообщение 'Вы угадали, поздравляем!'.

import random


def random_number_for_guessing():
	random_number = random.randrange(1, 101)
	return random_number


def guessing_numbers(hidden_number, user_number):
	while hidden_number != user_number:
		if user_number > hidden_number:
			print("Слишком много, попробуйте еще раз")
			user_number = processing_of_user_data()
			continue
		elif user_number < hidden_number:
			print("Слишком мало, попробуйте еще раз")
			user_number = processing_of_user_data()
			continue

	return "Вы угадали, поздравляем!"


def processing_of_user_data():
	user_number_correct = False
	print("Введите число от 1 до 100.")
	while user_number_correct == False:
		user_number = str(input("Ваше число:"))
		if "-" in user_number:
			print("Введите положительное число")
		elif "." in user_number:
			print("Введите натуральное число")
		elif user_number.isdigit() != True:
			print("Введите только число")
		elif 100 < int(user_number) or 1 > int(user_number):
			print("Введите числа от 1 до 100 ВКЛЮЧИТЕЛЬНО")
		else:
			user_number_correct = True
			return int(user_number)


rnd_num = random_number_for_guessing()
print("Привет! Это игра 'Угадайка'! Тебе нужно угадать число от 1 до 100.")
usr_num = processing_of_user_data()
print(guessing_numbers(rnd_num, usr_num))
