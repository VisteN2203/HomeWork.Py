from math import *

a, b, c = float(input()), float(input()), float(input())

if a != 0:
    D = pow(b, 2) - (4 * a * c)

    if D > 0:
        x1 = ((-b) - sqrt(D)) / (2 * a)
        x2 = ((-b) + sqrt(D)) / (2 * a)
        print(min(x1, x2), max(x1, x2), sep="\n")

    elif D == 0:
        x = - (b/(2 * a))
        print(x)

    else:
        print("Нет корней")
else:
    print("Число 'a' не может быть равно нулю")
