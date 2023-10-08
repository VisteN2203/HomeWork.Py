# объявление функции
def draw_box():
	star = "*"
	space = " "
	for i in range(1,15):
		if i == 1 or i == 14:
			print(star*10)
		else:
			print(star+space*8+star)
# основная программа
draw_box()  # вызов функции