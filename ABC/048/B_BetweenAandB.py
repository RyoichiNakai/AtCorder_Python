a, b, x = map(int, input().split())
# オーバーフロー
# cnt = len([_ for _ in range(a, b + 1, x)])
print(b // x - (a - 1) // x if a - 1 >= 0 else b // x - a // x + 1)

