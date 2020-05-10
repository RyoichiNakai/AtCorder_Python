n = int(input())
s = input()
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