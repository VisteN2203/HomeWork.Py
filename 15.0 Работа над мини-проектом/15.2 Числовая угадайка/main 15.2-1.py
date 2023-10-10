# Название Проекта - "Угадайка чисел"

# Описание проекта:
# программа генерирует случайное число в диапазоне от 1 до 100 и просит пользователя угадать это число.
# Если догадка пользователя больше случайного числа, то программа должна вывести сообщение
# 'Слишком много, попробуйте еще раз'. Если догадка меньше случайного числа, то программа должна вывести сообщение
# 'Слишком мало, попробуйте еще раз'. Если пользователь угадывает число, то программа должна поздравить его и
# вывести сообщение 'Вы угадали, поздравляем!'.

import random


def random_number(user_max_number):
	random_number = random.randrange(1, user_max_number + 1)
	return random_number


def guessing_numbers(hidden_number, user_number, user_max_number):
	count_of_attempts = 0
	while hidden_number != user_number:
		if user_number > hidden_number:
			print("Слишком много, попробуйте еще раз")
			user_number = processing_of_user_data(user_max_number)
			count_of_attempts += 1
			continue
		elif user_number < hidden_number:
			print("Слишком мало, попробуйте еще раз")
			user_number = processing_of_user_data(user_max_number)
			count_of_attempts += 1
			continue

	count_of_attempts += 1
	text1 = "Вы угадали, поздравляем!"
	text2 = f"Количество корректных попыток: {count_of_attempts}"
	return print(text1, text2, sep="\n")


def processing_of_user_data(user_num):
	user_number_correct = False
	print(f"Введите число от 1 до {user_num}.")
	while user_number_correct == False:
		user_number = str(input("Ваше число:"))
		if "-" in user_number:
			print("Введите положительное число")
		elif "." in user_number:
			print("Введите натуральное число")
		elif user_number.isdigit() != True:
			print("Введите только число")
		elif user_num < int(user_number) or 1 > int(user_number):
			print(f"Введите числа от 1 до {user_num} ВКЛЮЧИТЕЛЬНО")
		else:
			user_number_correct = True
			return int(user_number)


def restart_start_game(first_start):
	while True:
		if first_start > 0:
			print("Хочешь сыграть снова?")
		answer_user = str(input())
		first_start += 1
		answer_user_Yes = False
		list_answer_yes = ["Да", "да", "yes", "yep", "Yes", "y", "l", "lf", "L", "Y"]
		list_answer_no = ["Нет", "нет", "not", "nop", "Not", "ytn", "не"]
		if answer_user in list_answer_yes:
			answer_user_Yes = True
			return answer_user_Yes, first_start
			break
		elif answer_user in list_answer_no:
			print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
			return answer_user_Yes, first_start
			break
		else:
			print("Введите ответ 'Да' или 'Нет'")
			continue


first_start = 0
print("Привет! Это игра 'Угадайка'! Тебе нужно угадать число.\n"
	  "Хочешь поиграть?")
answer_user, first_start = restart_start_game(first_start)
while answer_user == True:
	print("Существует две версии игры.\n"
		  "1. версия: Тебе нужно угадать число от 1 до 100.\n"
		  "2. версия: Тебе нужно угадать число от 1 до любого числа которое захочешь.\n"
		  "Так в какую версию мы поиграем ? :) \n"
		  "(Напиши число)")
	version_game = int(input())
	if version_game == 1:
		user_max_number = 100
		rnd_nmb = random_number(user_max_number)
		prepositional_nmb = processing_of_user_data(user_max_number)
		guessing_numbers(rnd_nmb, prepositional_nmb, user_max_number)
		answer_user, first_start = restart_start_game(first_start)
	elif version_game == 2:
		print("Введи число максимальное число")
		user_max_number = int(input())
		rnd_nmb = random_number(user_max_number)
		prepositional_nmb = processing_of_user_data(user_max_number)
		guessing_numbers(rnd_nmb, prepositional_nmb, user_max_number)
		answer_user, first_start = restart_start_game(first_start)
	else:
		print("Указанно неверное значение")
		continue
