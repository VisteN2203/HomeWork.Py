# объявление функции
def convert_to_miles(km):
    miles = km * 0.6214
    return miles

# считываем данные
num = int(input())

# вызываем функцию
print(convert_to_miles(num))
