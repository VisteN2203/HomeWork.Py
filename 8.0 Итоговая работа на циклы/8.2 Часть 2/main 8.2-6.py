num = int(input())

lastNumber = 0
totalThree = 0
totalLastNumber = 0
totalEvenNumbers = 0
sumDigitsMoreFive = 0
productDigitsMoreSeven = 1
sumDigitsFiveOrZero = 0

flag = True

while num > 0:
	last_digit = num % 10
	if last_digit == 3:
		totalThree += 1

	if flag:
		lastNumber = last_digit
		flag = False

	if last_digit == lastNumber:
		totalLastNumber += 1

	if last_digit % 2 == 0:
		totalEvenNumbers += 1

	if last_digit > 5:
		sumDigitsMoreFive += last_digit
	num //= 10

	if last_digit > 7:
		productDigitsMoreSeven *= last_digit

	if last_digit == 0 or last_digit == 5:
		sumDigitsFiveOrZero += 1

print(totalThree,
	  totalLastNumber,
	  totalEvenNumbers,
	  sumDigitsMoreFive,
	  productDigitsMoreSeven,
	  sumDigitsFiveOrZero, sep="\n")
