from math import log

n = int(input())
one = 1
example = 0

for i in range(1,n+1):
    example = (one / i) + example
exampleTwo = example - log(n)
print(exampleTwo)
