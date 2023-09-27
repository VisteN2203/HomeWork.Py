n = int(input())

fibOne = fibTwo = 1

if n == 1:
    print(fibOne)
else:
    print(fibOne,fibTwo,end=" ")

if n <= 100:
    for i in range(2, n):
        fibOne, fibTwo = fibTwo, fibOne + fibTwo
        print(fibTwo, end=" ")
