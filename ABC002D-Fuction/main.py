from itertools import combinations

n, m = map(int, input().split())
s = set(tuple(map(int, input().split())) for i in range(m))
print(s)

for i in range(n, 0, -1):
    cbn = combinations(range(1, n + 1), i)
    for c in cbn:
        if len(set(combinations(c, 2)) - s) == 0:
            print(len(c))
            exit(0)

# 派閥がn人いるときの人数の組み合わせを全て出す
# その中の2人組の組み合わせを算出
# その組み合わせと与えられた関係の差集合がφになる時
# 議員が最大になるためその時の値を出力
# forを逆側から参照すれば最大値を1発で求めることができる
# 最大値を求めるプログラムだからいけてるところはある

# from itertools import product
# n, m = map(int, input().split())
# xy = [list(map(int, input().split())) for _ in range(m)]
#
# mem = [i + 1 for i in range(n)]
# flag = False
# ans = 0
# res = 0
# for i in range(m):
#     fuc = mem[xy[i][0] - 1:xy[i][1]]
#     cnt = 0
#     for prd in product(fuc, repeat=2):
#         if list(prd)[0] == list(prd)[1] or list(prd)[0] >= list(prd)[1]:
#             continue
#
#         if list(prd) in xy:
#             cnt += 1
#
#     if cnt > ans:
#         ans = cnt
#         res = len(fuc)
#
# print(res)
