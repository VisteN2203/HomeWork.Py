text = str(input())

i = 0
while text not in ("стоп","хватит","достаточно"):
    i += 1
    text = str(input())
print(i)