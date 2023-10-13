# объявление функции
def draw_triangle():
	space = " "
	total_star = 1
	max_star = 15
	for i in range(8, 0, -1):
		spaces = space * (i - 1)
		if total_star > max_star:
			break
		else:
			data = spaces + (total_star * "*")
			total_star += 2
			print(data)

# основная программа
draw_triangle()  # вызов функции