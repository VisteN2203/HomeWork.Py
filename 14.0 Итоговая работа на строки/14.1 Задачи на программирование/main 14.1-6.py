# объявление функции
def get_month(language, number):
	month = [[],['','январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь'],
			 ['','january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
			  'november', 'december']]
	if language == "ru":
		num_list = 1
	else:
		num_list = 2

	return month[num_list][number]

# считываем данные
lan = str(input())
num = int(input())

# вызываем функцию
print(get_month(lan, num))
