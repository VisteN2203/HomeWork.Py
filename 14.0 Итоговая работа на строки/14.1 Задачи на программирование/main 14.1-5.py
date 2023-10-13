# объявление функции
def number_to_words(num):
	list_of_num = [" ", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
	list_of_digit = ["", "десять", "надцать", ]
	list_of_digit2 = ["дцать", "", "десят", "", "сорок", "", "", "", "", "девяносто"]

	if num <= 9:
		return list_of_num[num]

	if 10 <= num <= 99:

		num1 = str(num)[0:1]
		num2 = str(num)[1:]

		num1 = int(num1)
		num2 = int(num2)

		if num1 == 1:
			if num2 == 0:
				return list_of_digit[num1]
			elif num2 == 2:
				return list_of_num[num2][:2] + "е" + list_of_digit[num1 + 1]
			elif num2 == 1 or num2 == 3:
				return list_of_num[num2] + list_of_digit[num1 + 1]
			else:
				return list_of_num[num2][:len(list_of_num[num2]) - 1] + list_of_digit[num1 + 1]


		if num1 == 4:
			if num2 == 0:
				return list_of_digit2[num1]
			else:
				return list_of_digit2[num1] + " " + list_of_num[num2]

		if num1 == 9:
			if num2 == 0:
				return list_of_digit2[num1]
			else:
				return list_of_digit2[num1] + " " + list_of_num[num2]

		if 2 <= num1 <= 3:
			if num2 == 0:
				return list_of_num[num1] + list_of_digit2[0]
			else:
				return list_of_num[num1] + list_of_digit2[0] + " " + list_of_num[num2]

		if 5 <= num1 <= 8:
			if num2 == 0:
				return list_of_num[num1] + list_of_digit2[2]
			else:
				return list_of_num[num1] + list_of_digit2[2] + " " + list_of_num[num2]

# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))
