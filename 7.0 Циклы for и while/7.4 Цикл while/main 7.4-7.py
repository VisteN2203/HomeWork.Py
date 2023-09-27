totalMoney = int(input())

mintedCoin = 0

while totalMoney > 0:
    if totalMoney - 25 >= 0:
        mintedCoin += 1
        totalMoney -= 25

    elif totalMoney - 10 >= 0:
        mintedCoin += 1
        totalMoney -= 10

    elif totalMoney - 5 >= 0:
        mintedCoin += 1
        totalMoney -= 5

    elif totalMoney - 1 >= 0:
        mintedCoin += 1
        totalMoney -= 1

print(mintedCoin)