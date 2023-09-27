number = int(input())

maximum = 0
minimum = 9
while number != 0:
    remains = number % 10
    maximum = max(maximum, remains)
    minimum = min(minimum,remains)
    number //= 10


print(f"Максимальная цифра равна {maximum}")
print(f"Минимальная цифра равна {minimum}")