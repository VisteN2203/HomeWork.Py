# объявление функции
def print_digit_sum(num):
	total = 0
	while num > 0:
		counter = num % 10
		total += counter
		num //= 10
	print(total)
# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)