from itertools import product

n = int(input())
t = [int(input()) for _ in range(n)]
res = 10000000
# こっちの方が冗長性もなくてすっきりしてるかな
for prd in product([0, 1], repeat=n):
    y1 = []
    y2 = []
    for i, j in zip(t, prd):
        if j == 1:
            y1.append(i)
        else:
            y2.append(i)
    ans = max(sum(y1), sum(y2))
    res = min(res, ans)
print(res)


# この回答でも大丈夫だったが、
# この回答では肉を焼く時間がどれかと同じの時にうまくいかない(例: 4 4 4 4)
# n = int(input())
# t = [int(input()) for _ in range(n)]
# res = 100000000
# for i in product(t, repeat=n):
#     y1 = list(set(i))
#     y2 = list(set(t) - set(i))
#     ans = max(sum(y1), sum(y2))
#     res = min(res, ans)
# print(res)
