# объявление функции
def is_magic(date):
	date_first = date[0:2]
	date_second = date[3:5]
	date_thread = date[8:10]
	list = [int(date_first),int(date_second),int(date_thread)]
	if list[0] * list[1] == list[2]:
		return True
	else:
		return False

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))