number = int(input())

firstNumber = number // 100
secondNumber = (number//10) % 10
thirdNumber = number % 10

maximum = max(firstNumber, secondNumber, thirdNumber)
minimum = min(firstNumber, secondNumber, thirdNumber)

average = maximum - minimum

if ((firstNumber + secondNumber + thirdNumber) - maximum - minimum) == average:
    print("Число интересное")
else:
    print("Число неинтересное")


