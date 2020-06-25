# 方針：与えられた配列を逆から全探索していく
# bit全探索でとく？？
# todo:下のコードの解き方を理解する
from itertools import product

D, G = map(int, input().split())

prob = []
for j in range(1, D + 1):
    p, c = map(int, input().split())
    prob.append((j * 100, p, c))  # score,amount,bonus

print(prob)
ans = -1
for prd in product([0, 1], repeat=D):
    print(prd)
    cnt = 0
    g = 0
    for j, (score, amount, bonus) in zip(prd, prob):
        print(j, (score, amount, bonus))
        if j:
            cnt += amount
            g += score * amount + bonus

    if g < G:
        for j, (score, amount, bonus) in reversed(tuple(zip(prd, prob))):
            if (not j) and (score * amount >= G - g):
                use = (G - g + score - 1) // score
                cnt += use
                g += score * use
                break

    if (g < G) or (~ans and ans <= cnt):
        continue
    ans = cnt

print(ans)

"""
d, g = map(int, input().split())
num_bonus = [list(map(int, input().split())) for _ in range(d)]

num_bonus.reverse()
score = 0
cnt = 0
p_i = d

for i in range(d):

    for j in range(num_bonus[i][0]):
        cnt += 1
        score += 100 * p_i
        if score >= g:
            print(cnt)
            exit(0)

    score += num_bonus[i][1]
    p_i -= 1

"""

# オーバーフロー（bit全探索しすぎた）
# このやり方だとボーナスの考え方を導入できない
# d, g = map(int, input().split())
# num_bonus = [list(map(int, input().split())) for _ in range(d)]
# num = 0
# score_list = []
# res = 0
#
# for i in range(d):
#     num += num_bonus[i][0]
#     for j in range(num_bonus[i][0]):
#         score_list.append(100 * (i + 1))
#
# for i in range(2 ** num):
#     bit_list = []
#     all_score = 0
#     cnt = 0
#
#     for j in range(num):
#         if (i >> j) & 1:
#             cnt += 1
#             bit_list.append(1)
#         else:
#             bit_list.append(0)
#
#     for j in range(num):
#         all_score += score_list[j] * bit_list[j]
#
#     print(all_score, cnt, bit_list)
#
#     if all_score >= g:
#         res = min(res, cnt)
#
# print(res)
