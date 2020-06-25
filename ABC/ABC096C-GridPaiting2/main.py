h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
dx = [-1, 0, 1]
dy = [-1, 0, 1]

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            flag = 0
            for d_x in dx:
                for d_y in dy:
                    if (d_x == 0 and d_y == 0) or (d_x == -1 and d_y == -1) or (d_x == 1 and d_y == 1)\
                            or (d_x == 1 and d_y == -1) or (d_x == -1 and d_y == 1):
                        # 斜め方向はcontinue
                        continue
                    if 0 <= i + d_x < h and 0 <= j + d_y < w \
                            and s[i + d_x][j + d_y] == '#':
                        flag = 1

            if flag == 0:
                print('No')
                exit(0)

print('Yes')

# リファクタリング
# 斜め方向気にしないならこれでもあり
for i in range(h):
    for j in range(w):
        if s[i][j] == "#" and 0 <= i - 1 < h and 0 <= j - 1 < w and 0 <= i + 1 < h and 0 <= j + 1 < w:
            if s[i - 1][j] != "#" and s[i][j - 1] != "#" and s[i][j + 1] != "#" and s[i + 1][j] != "#":
                print("No")
                exit(0)
print('Yes')
