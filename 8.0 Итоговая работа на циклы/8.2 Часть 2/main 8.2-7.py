import math

Number = 0
finaFirstSum = 0
finalSecondSum = 0

for i in range(1, 33):
	for j in range(1,33):
		for k in range(1,33):
			for n in range(1,33):
				FirstCube = math.pow(i,3) + math.pow(j,3)
				SecondCube = math.pow(n,3) + math.pow(k,3)
				firstSum = i + j
				secondSum = k + n
				if FirstCube == SecondCube and i != j and i != n and i != k and j != n and j != k:
					if i != j and i != n and i != k and j != n and j != k:
						if firstSum != finaFirstSum and secondSum != finalSecondSum:
							finaFirstSum = firstSum
							finalSecondSum = secondSum
							print("i = ", i)
							print("j = ", j)
							print("n = ", n)
							print("k = ", k)
							print(int(FirstCube))
