def start():
	print("Вас приветствует программа 'Помощник Цезаря'!\n"
		  "С помощью этой программы вы можете:\n"
		  "Первое: Шифровать или Дешифровать.\n"
		  "Второе: Использовать русский или английский язык.\n"
		  "Третье: Изменять шаг сдвига.\n")

def first_role():
	while True:
		print("Будем Шифровать или Дешифровать;1 - Шифровать, 2 - Дешифровать")
		response = str(input())
		flag_first_role = False
		if response == "1":
			flag_first_role = True
			return flag_first_role
		elif response == "2":
			return  flag_first_role
		else:
			continue

def second_role():
	while True:
		print("Будем использовать русский или английский язык;1 - Русский язык, 2 - Английский язык")
		response = str(input())
		flag_second_role = False
		if response == "1":
			flag_second_role = True
			return flag_second_role
		elif response == "2":
			return flag_second_role
		else:
			continue

def third_role():
	while True:
		print("Сколько символов должен быть сдвиг?")
		response = str(input())
		if response.isdigit() == True:
			response = int(response)
			if response > 0:
				return response
			else:
				print("Введите число больше нуля!")
				continue
		else:
			print("Введите число!")
			continue

def caesars_cipher(fr,sr,rtr):
	print("Введите текст для изменения его:")
	text = str(input())
	# Если Первое Правило "Тру", то шифруем
	if fr == True:
		# Если Второе Правило "Тру", то русский язык
		if sr == True:
			new_text = ""
			for i in range(0,len(text)):
				letter_ord = ord(text[i])
				if 1040 <= letter_ord <= 1103:
					if letter_ord + rtr > 1103:
						new_text_1 = chr(((letter_ord + rtr) - 1103) + 1039)
						new_text += new_text_1.lower()
					else:
						new_text += chr(letter_ord + rtr)
				else:
					new_text += text[i]
			return new_text
		# Если Второе Правило "Фолс", то английский язык
		elif sr == False:
			new_text = ""
			for i in range(0,len(text)):
				letter_ord = ord(text[i])
				if 65 <= letter_ord <= 90:
					if letter_ord + rtr > 90:
						new_text += chr(((letter_ord + rtr) - 90) + 64)
					else:
						new_text += chr(letter_ord + rtr)
				elif 97 <= letter_ord <= 122:
					if letter_ord + rtr > 122:
						new_text += chr(((letter_ord + rtr) - 122) + 96)
					else:
						new_text += chr(letter_ord + rtr)
				else:
					new_text += text[i]
			return new_text
	# Если Первое Правило "Фолс", то дешифруем
	elif fr == False:
		# Если Второе Правило "Тру", то русский язык
		if sr == True:
			new_text = ""
			for i in range(0,len(text)):
				letter_ord = ord(text[i])
				if 1040 <= letter_ord <= 1071:
					if letter_ord - rtr < 1040:
						new_text += chr(1071 - (letter_ord - rtr) + 1039)
						continue
					else:
						new_text += chr(letter_ord - rtr)
						continue
				if 1072 <= letter_ord <= 1103:
					if letter_ord - rtr < 1072:
						new_text_1 = chr(letter_ord - rtr)
						new_text += new_text_1.lower()
						continue
					else:
						new_text += chr(letter_ord - rtr)
						continue
				else:
					new_text += text[i]
					continue
			return new_text
	# 	# Если Второе Правило "Фолс", то английский язык
		elif sr == False:
			new_text = ""
			for i in range(0, len(text)):
				letter_ord = ord(text[i])
				if 65 <= letter_ord <= 90:
					if letter_ord - rtr < 65:
						new_text += chr(90 - 64 + (letter_ord - rtr))
					else:
						new_text += chr(letter_ord - rtr)
				elif 97 <= letter_ord <= 122:
					if letter_ord - rtr < 97:
						new_text += chr(122 - 96 + (letter_ord - rtr))
					else:
						new_text += chr(letter_ord - rtr)
				else:
					new_text += text[i]
			return new_text

start()
flag_first_role = first_role()
flag_second_role = second_role()
response_third_role = third_role()
print(caesars_cipher(flag_first_role,flag_second_role,response_third_role))

