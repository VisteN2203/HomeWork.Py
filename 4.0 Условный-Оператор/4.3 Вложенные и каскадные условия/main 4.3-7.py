colorOne, colorTwo = str(input()), str(input())

if (colorOne == "красный" and colorTwo == "синий") or (colorOne == "синий" and colorTwo == "красный"):
    print("фиолетовый")

elif (colorOne == "красный" and colorTwo == "желтый") or (colorOne == "желтый" and colorTwo == "красный"):
    print("оранжевый")

elif (colorOne == "синий" and colorTwo == "желтый") or (colorOne == "желтый" and colorTwo == "синий"):
    print("зеленый")

elif(colorOne == "синий" or colorOne == "красный" or colorOne == "желтый") and (colorOne == colorTwo):
    print(colorOne)

else:
    print("ошибка цвета")