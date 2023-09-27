age = int(input())

if(age <= 13):
    print("детство")
else:
    if(14 <= age <= 24):
        print("молодость")
    else:
        if(25 <= age <= 59):
            print("зрелость")
        else:
            print("старость")