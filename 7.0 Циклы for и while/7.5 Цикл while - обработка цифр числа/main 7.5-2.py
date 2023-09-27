number = int(input())

while number != 0:
    Remains = number % 10
    print(Remains, end="")
    number //= 10
