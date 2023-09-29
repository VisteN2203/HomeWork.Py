
num = int(input())

maxNumber = -1

while num != 0:
    lastDigit = num % 10
    if lastDigit % 3 == 0:
        if maxNumber < lastDigit:
            maxNumber = lastDigit
    num //= 10

if maxNumber == -1:
    print("NO")
else:
    print(maxNumber)



# Прошлый код
# n = int(input())
# max_digit = n % 10
# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit < max_digit:
#             digit = max_digit
#     n = n % 10
# if max_digit == 0:
#     print('NO')
# else:
#     print(max_digit)