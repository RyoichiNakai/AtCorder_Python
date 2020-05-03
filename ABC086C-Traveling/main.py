N = int(input())
t = [0] * (N + 1)
x = [0] * (N + 1)
y = [0] * (N + 1)
for i in range(N):
    t[i + 1], x[i + 1], y[i + 1] = map(int, input().split())

for i in range(N):
    dt = t[i + 1] - t[i]
    dist = abs(x[i + 1] - x[i]) + abs(y[i + 1] - y[i])
    if dt < dist:
        print("No")
        exit(0)

    if dist % 2 != dt % 2:
        print("No")
        exit(0)

print("Yes")

# 別解
# for _ in range(int(input())): (_は使わない時に役立つそう)
# t, x, y = map(int, input().split())
#  if (x + y + t) % 2 or (x + y) > t:
#    print('No')
#    exit(0)

a = 2

if a % 2:  # 奇数だと判定(a % 2 == 1)
    print('even')
else:
    print('odd')
