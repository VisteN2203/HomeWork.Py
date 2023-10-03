text = str(input())

if text.count("f") == 1:
	print(text.find("f"))

elif text.count("f") >= 2:
	print(text.find("f"),text.rfind("f"), end="")
	
else:
	print("NO")

