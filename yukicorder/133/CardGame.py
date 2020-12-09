import itertools
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
rest = 0
win = 0

for i in a:
    for j in b:
        rest += 1
        if i > j:
            win += 1

print(win/rest)
