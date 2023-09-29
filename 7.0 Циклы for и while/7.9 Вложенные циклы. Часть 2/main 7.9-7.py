a, b = int(input()), int(input())

if a < b:

	for i in range(a, b + 1):
		total = 0

		for j in range(2, b + 1):
			calculations = i % j

			if calculations == 0:
				total += 1

		if total == 1:
			print(i)
