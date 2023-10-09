import math
# объявление функции
def solve(a, b, c):
	if a != 0:
		D = math.pow(b, 2) - (4 * a * c)
		if D > 0:
			x1 = ((-b) - math.sqrt(D)) / (2 * a)
			x2 = ((-b) + math.sqrt(D)) / (2 * a)
			return min(x1, x2), max(x1, x2)
		elif D == 0:
			x = - (b / (2 * a))
			return x,x
		else:
			print("Нет корней")

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
