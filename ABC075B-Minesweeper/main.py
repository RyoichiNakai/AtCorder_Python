h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
dx = [-1, 0, 1]
dy = [-1, 0, 1]

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            for d_x in dx:
                for d_y in dy:
                    if 0 <= i + d_x < h and 0 <= j + d_y < w and s[i + d_x][j + d_y] != '#':
                        if s[i + d_x][j + d_y] == '.':
                            s[i + d_x][j + d_y] = 1
                        else:
                            s[i + d_x][j + d_y] += 1
# elseにcontinueかかん方が実行時間早いかな

for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            s[i][j] = 0
        print(s[i][j], end='')  # 改行せずにprint
    print()
