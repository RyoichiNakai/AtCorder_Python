n = int(input())
change = 1000 - n

coins = [500, 100, 50, 10, 5, 1]
ans = 0

while coins:
    coin = coins.pop(0)
    ans += change // coin
    change = change % coin

print(ans)
