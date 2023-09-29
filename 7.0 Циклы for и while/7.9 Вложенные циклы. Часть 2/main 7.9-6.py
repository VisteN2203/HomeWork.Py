from math import factorial

n = int(input())

sum = 1
#
# for i in range(1,n + 1):
# 	pov = factorial(i)
# 	sum += pov
# print(sum)

sumFact = 0
for i in range(1, n + 1):
	for j in range(1,i+1):
		sum *= j
	sumFact += sum
	sum	= 1

print(sumFact)
