num1,num2,num3,num4 = int(input()),int(input()),int(input()),int(input())

if (num1<num2<num3<num4):
    print(num1)
else:
    if (num2<num3<num4):
        print(num2)
    else:
        if(num3<num4):
            print(num3)
        else:
            print(num4)