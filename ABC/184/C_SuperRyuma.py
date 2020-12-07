a, b = map(int, input().split())
c, d = map(int, input().split())

cnt = 0
if a + b == c + d or a - b == c - d or abs(a - c) + abs(b - d) <= 3:
    cnt += 1

print(cnt)
