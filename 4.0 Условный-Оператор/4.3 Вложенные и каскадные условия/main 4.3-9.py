a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

if a2 < a1:
    # теперь отрезок a1, b1 точно левее (по крайней мере своим левым концом) отрезка a2, b2
    a1, b1, a2, b2 = a2, b2, a1, b1

if a2 > b1:
    print("пустое множество")
elif a2 == b1:
    print(a2)
else:
    if b1 < b2:
        print(a2, b1)
    else:
        print(a2, b2)