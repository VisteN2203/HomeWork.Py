text = str(input())

firstH = text.find("h")
secondH = text.rfind("h")
textOld = ""

for i in range(firstH,secondH + 1):
	textOld += text[i]

print(text.replace(textOld, ""))
