n = int(input())
s = input()

# 下の回答だとタイムオーバー(O(n^2))
ans = n
for i in range(n):
    cnt = 0
    for j in range(i):
        if s[j] == "W":
            cnt += 1
    for k in range(i + 1, n):
        if s[k] == "E":
            cnt += 1

    ans = min(cnt, ans)

print(ans)

w_e = [0] * n
e_w = [0] * n
ans = []

# 別解
# 5
# WEEWW
# [0, 1, 1, 1, 2] [2, 1, 0, 0, 0]
# 1
for i in range(n - 1):
    # リーダより西側にいる人のなかで西に向いている人が東側に向くようにする(以下、反対向きの人と略)
    # 累積和の考え方を用いて今のリーダの反対向きの人の数は前のリーダのそれに＋１してあげればいい
    if s[i] == 'W':
        w_e[i + 1] = w_e[i] + 1
    else:
        w_e[i + 1] = w_e[i] + 0

for i in range(n - 2, -1, -1):  # 右側は開区間と覚えておく！！
    if s[i + 1] == 'E':
        e_w[i] = e_w[i + 1] + 1
    else:
        e_w[i] = e_w[i + 1] + 0

for i in range(n):
    ans.append(w_e[i] + e_w[i])

print(min(ans))
