number = int(input())

sum, i,composition = 0, 0, 1

while number != 0:
    remains = number % 10
    if i == 0:
        saveLastNum = remains
    sum += remains
    i += 1
    composition *= remains
    if number >= 0:
        saveFirstNum = number
    number //= 10

arithmeticMean = sum / i
sumFirstAndLastNum = saveFirstNum + saveLastNum

print(sum, i, composition, arithmeticMean,saveFirstNum, sumFirstAndLastNum, sep="\n")
