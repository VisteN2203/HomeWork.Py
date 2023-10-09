# объявление функции
def convert_to_python_case(text):
	space = "_"
	new_text = ""
	for i in range(0,len(text)):
		if 90 >= ord(text[i]) >= 65 and i != 0:
			new_text += space + text[i]
		else:
			new_text += text[i]

	return new_text.lower()

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
