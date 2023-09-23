number = int(input())

if 2 <= number <= 5:
    if number %2 == 0:
        print("NO")
    else:
        print("YES")

elif 6 <= number <= 20:
    if number % 2 == 0:
        print("YES")
    else:
        print("NO")

elif number % 2 == 0 and number > 20:
    print("NO")

else:
    print("YES")

