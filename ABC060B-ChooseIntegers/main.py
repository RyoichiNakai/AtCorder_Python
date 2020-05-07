a, b, c = map(int, input().split())

for i in range(b):  # あまりのパターンがb個しかない
    if a * (i + 1) % b == c:
        print('YES')
        exit(0)

print('NO')
