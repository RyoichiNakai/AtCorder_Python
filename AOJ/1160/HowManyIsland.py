import sys
sys.setrecursionlimit(10 ** 7)  # 再帰関数の呼び出し制限

width, height = map(int, input().split())
c = [list(map(int, input().split())) for i in range(height)]

dx = [-1, 0, 1]
dy = [-1, 0, 1]
cnt = 0


def dfs(x, y):
    if not (0 <= x < height) or not (0 <= y < width) or (c[x][y] == 0) or (c[x][y] == -1):
        # 壁に当たったり、探索範囲外になったり，探索済だった場合はreturn
        return

    c[x][y] = -1  # 探索済みを示すためのマーキング

    # 再帰で探索を行う
    for d_x in dx:
        for d_y in dy:
            if d_x == 0 and d_y == 0:
                continue
            dfs(x + d_x, y + d_y)


for i in range(height):
    for j in range(width):
        if c[i][j] == 0 or c[i][j] == -1:  # 探索済と海ならばcontinue
            continue

        dfs(i, j)  # スタート位置，陸の場合のみdfsする
        cnt += 1

print(cnt)
