# объявление функции
def get_shipping_cost(quantity):
	if quantity == 1:
		return quantity * 1000
	else:
		return 1000 + ((quantity-1) * 120)

# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))