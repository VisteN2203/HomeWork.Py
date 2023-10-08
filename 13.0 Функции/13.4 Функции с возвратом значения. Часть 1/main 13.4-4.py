# объявление функции
def number_of_factors(num):
	list = [i for i in range(1, num // 2 + 1) if num % i == 0]
	list.append(num)
	return len(list)


# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))
