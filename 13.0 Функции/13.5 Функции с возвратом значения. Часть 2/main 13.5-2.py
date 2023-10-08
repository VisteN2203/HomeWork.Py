# объявление функции
def is_prime(num):
	total = 0
	for i in range(2, num + 1):
		if num % i == 0:
			total += 1
	return total == 1



# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))