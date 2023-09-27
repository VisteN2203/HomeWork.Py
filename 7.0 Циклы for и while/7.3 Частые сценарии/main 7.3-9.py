n = int(input())

maxOne , maxTwo = -1, -1

if n >= 2:
    for i in range(n):
        nTwo = int(input())
        if nTwo > maxOne:
            maxOne, maxTwo = nTwo, maxOne
        elif nTwo > maxTwo:
            maxTwo = nTwo

print(maxOne, maxTwo, sep="\n")
