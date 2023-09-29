allHead = 100
allMoney = 100

for b in range(1, 101):
    for k in range(1, 101):
        for t in range(1, 101):
            totalMoney = b * 10 + k * 5 + t * 0.5
            totalHead = b + k + t
            if totalHead == allHead and totalMoney == allMoney:
                print("n =",b,"k =",k,"t =",t)