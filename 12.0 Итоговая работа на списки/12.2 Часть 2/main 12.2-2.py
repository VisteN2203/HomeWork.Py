L = list(str(input()).split())
M = list(str(input()).split())

listThree = []

if len(L) == len(M):
	for i in range(len(L)):
		listThree.append(int(L[i]) + int(M[i]))

print(*listThree)