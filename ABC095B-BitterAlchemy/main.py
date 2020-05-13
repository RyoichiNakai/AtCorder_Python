n, x = map(int, input().split())
m = [int(input()) for _ in range(n)]

for i in range(n):
    x -= m[i]

if x == 0:
    print(n)
else:
    print(n + x // min(m))
