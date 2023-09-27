from math import *

a, b = float(input()), float(input())

ArithmeticMeanOfNumbers = (a + b) / 2
GeometricMeanOfNumbers = sqrt(a * b)
HarmonicMeanOfNumbers = (2 * a * b) / (a + b)
QuadraticMeanOfNumbers = sqrt(((pow(a, 2)) + pow(b, 2)) / 2)

print(ArithmeticMeanOfNumbers, GeometricMeanOfNumbers,
      HarmonicMeanOfNumbers, QuadraticMeanOfNumbers, sep="\n")

