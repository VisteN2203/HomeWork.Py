num = int(input())

if num == 0:
    print("зеленый")
elif 1 <= num <= 10:
    if num % 2 == 0:
        print("черный")
    else:
        print("красный")

elif 11 <= num <= 18:
    if num % 2 == 0:
        print("красный")
    else:
        print("черный")

elif 19 <= num <= 28:
    if num % 2 == 0:
        print("черный")
    else:
        print("красный")

elif 29 <= num <= 36:
    if num % 2 == 0:
        print("красный")
    else:
        print("черный")

else:
    print("ошибка ввода")