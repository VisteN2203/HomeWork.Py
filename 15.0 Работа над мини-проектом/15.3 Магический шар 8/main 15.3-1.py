import random
import time


def answers():
	list_good_response = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом"]
	list_hesitantly_positive_response = ["Мне кажется - да", "Вероятнее всего", "Хорошие перспективы",
										 "Знаки говорят - да", "Да"]
	list_neutral_response = ["Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать",
							 "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять"]
	list_negative_response = ["Даже не думай", "Мой ответ - нет", "По моим данным - нет",
							  "Перспективы не очень хорошие", "Весьма сомнительно"]

	random_list = random.randrange(0, 4)
	random_num_answer = random.randrange(0, 5)
	all_list_response = [list_good_response, list_hesitantly_positive_response,
						 list_neutral_response, list_negative_response]

	need_list = all_list_response[random_list]
	need_response = need_list[random_num_answer]
	return need_response


def start_game():
	print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
	print("Как тебя зовут?")
	name = str(input())
	print(f"Привет {name.capitalize()}!")
	return name


def restart_game(name_user, total_restart):
	while True:
		if total_restart == 0:
			print(f"{name_user.capitalize()}, хочешь получить ответ на любой твой вопрос?")
		else:
			print(f"{name_user.capitalize()}, хочешь еще получить ответ на любой твой вопрос?")
		answer_user = str(input())
		answer_user_Yes = False
		list_answer_yes = ["Да", "да", "yes", "yep", "Yes", "y", "l", "lf", "L", "Y", "д", "дя", "Дя"]
		list_answer_no = ["Нет", "нет", "not", "nop", "Not", "ytn", "не"]
		if answer_user in list_answer_yes:
			answer_user_Yes = True
			return answer_user_Yes
		elif answer_user in list_answer_no:
			print("Возвращайся если возникнут вопросы!")
			return answer_user_Yes
		else:
			print("Введите ответ 'Да' или 'Нет'")
			continue


def answer_to_questions(name_user):
	print(f"{name_user.capitalize()}! На какой вопрос ты хочешь получить ответ?")
	print("Напиши мне свой вопрос ...")
	question_user = str(input())
	time.sleep(1)
	response = answers()
	return print(f"{name_user.capitalize()}, {response.lower()}")


name_user = start_game()
total_restart = 0
answer_user = restart_game(name_user, total_restart)
total_restart += 1
while answer_user == True:
	answer_to_questions(name_user)
	time.sleep(3)
	answer_user = restart_game(name_user, total_restart)
