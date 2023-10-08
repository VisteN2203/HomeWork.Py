string = str(input())

list = [string[i] for i in range(len(string)) if string[i] in "0123456789"]


print(*list,sep="")