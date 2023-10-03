text = str(input())

findFirstH = text.find("h")
findSecondH = text.rfind("h")

print(text[:findFirstH + 1],end="")
print(text[findSecondH-1:findFirstH: -1], end="")
print(text[findSecondH:],end="")
