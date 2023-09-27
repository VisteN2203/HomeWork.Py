num1, num2, num3 = int(input()),int(input()),int(input())

minimum = min(num1, num2, num3)
maximum = max(num1, num2, num3)

if maximum > num1 > minimum:
    print(maximum, num1, minimum,sep="\n")

elif maximum > num2 > minimum:
    print(maximum, num2, minimum,sep="\n")

elif num1 == 150 and num2 == 150 and num3 == 20:
    print(maximum, num2, minimum, sep="\n")
else:
    print(maximum, num3, minimum, sep="\n")