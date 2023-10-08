# объявление функции
import math

def get_next_prime(num):
	return_num = 0
	while return_num == 0:
		num += 1
		total = 0
		for i in range(2, num + 1):
			if num % i == 0:
				total += 1
		if total == 1:
			return_num = num
			return return_num

	# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
