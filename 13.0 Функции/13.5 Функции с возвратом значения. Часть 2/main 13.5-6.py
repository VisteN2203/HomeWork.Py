# объявление функции
def is_palindrome(text):
	list = [text[i].lower() for i in range(len(text.lower())) if text[i] not in " ,.!?-"]
	list_revers = list[::-1]
	if list == list_revers:
		flag = True
	else:
		flag = False

	return flag

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))