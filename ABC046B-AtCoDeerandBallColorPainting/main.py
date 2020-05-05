n, k = map(int, input().split())
c = k
for _ in range(n - 1):
    c = c * (k - 1)
    c = c % (2 ** 31 - 1)
print(c)
