from math import *

x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())

EuclideanDistance = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

print(EuclideanDistance)
