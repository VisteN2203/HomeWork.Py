number = int(input())

while number >= 99:
    remains = number % 10
    number //= 10

number %= 10

print(number)