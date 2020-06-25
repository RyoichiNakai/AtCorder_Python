a, b, c, x, y = map(int, input().split())

price = a * x + b * y

if (a + b) // 2 >= c:
    if x >= y:
        price = min(2 * x * c, 2 * y * c + (x - y) * a)

    else:
        price = min(2 * x * c + (y - x) * b,  2 * y * c)

print(price)
