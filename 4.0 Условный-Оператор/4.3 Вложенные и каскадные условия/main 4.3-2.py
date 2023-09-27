num1,num2,num3 = int(input()),int(input()),int(input())

if(num1 == num2 == num3):
    print("Равносторонний")
elif(num1==num2 or num2==num3 or num3==num1):
    print("Равнобедренный")
else:
    print("Разносторонний")