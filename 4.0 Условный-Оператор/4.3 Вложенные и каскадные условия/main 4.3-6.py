num1, num2, string = int(input()), int(input()), str(input())

if string == "*":
    print(num1*num2)

elif string == "+":
    print(num1+num2)

elif string == "-":
    print(num1-num2)

elif string == "/":
    if num2 == 0:
        print("На ноль делить нельзя!")
    else:
        print(num1/num2)

else:
    print("Неверная операция")