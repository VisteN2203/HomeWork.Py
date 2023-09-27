num = int(input())

num1 = num % 10
num2 = (num % 100) // 10
num3 = num // 100

amount = num1 + num2 + num3
compositions = num1 * num2 * num3

print("Сумма цифр =", amount)
print("Произведение цифр =",compositions)

