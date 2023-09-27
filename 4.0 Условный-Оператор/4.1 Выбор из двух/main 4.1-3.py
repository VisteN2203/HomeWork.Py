number = int(input())

num1 = number // 1000
num2 = number // 100 % 10
num3 = (number % 100) // 10
num4 = number % 10

data1 = num1 + num4

data2 = num2 - num3

if (data1 == data2):
    print("ДА")
else:
    print("НЕТ")