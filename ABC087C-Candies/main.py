n = int(input())
a = [list(map(int, input().split())) for _ in range(2)]
cntList = []

for i in range(n):
    cnt = 0
    for j in range(i + 1):
        cnt += a[0][j]

    for k in range(i, n):
        cnt += a[1][k]

    cntList.append(cnt)

print(max(cntList))

# 別解
res = 0
for i in range(n):
    tmp1 = sum(a[0][:i+1])  # その番号まで欲しかったら＋１すること(例a[:0] = [], a[:1] = [3]
    tmp2 = sum(a[1][i:])    # スライスは各indexの間のイメージ
    print(tmp1 + tmp2)
    res = max(res, tmp1 + tmp2)
print(res)




