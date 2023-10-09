# объявление функции
def is_correct_bracket(text):
	list_bracket = [text[i] for i in range(len(text))]
	is_correct_bracket = False
	count = 0
	for i in range(len(list_bracket)):
		if list_bracket[i] == "(":
			count += 1
		if list_bracket[i] == ")":
			count -= 1
		if count < 0:
			break

	if count == 0:
		is_correct_bracket = True
		return is_correct_bracket
	else:
		return is_correct_bracket

# считываем данные
txt = str(input())

# вызываем функцию
print(is_correct_bracket(txt))
