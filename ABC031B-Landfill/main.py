import sys

sys.setrecursionlimit(10 ** 8)  # 再帰関数の呼び出し制限
c = [list(input()) for i in range(10)]


# todo: 陸と海を逆にして考えてみる(line10 'x' => 'o', line41)
def dfs(x, y):
    flag = False
    if not (0 <= x < 10) or not (0 <= y < 10) or c[x][y] == 'x' or c[x][y] == '#':  # 壁に当たったり、探索範囲外になった場合はreturn
        return

    c[x][y] = "#"  # 探索済みを示すためのマーキング
    dx_dy_1 = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    dx_dy_2 = [[2, 0], [-2, 0], [0, 2], [0, -2]]

    mass_1 = ''
    mass_2 = ''
    for i in range(4):
        if 0 <= x + dx_dy_2[i][0] < 10 and 0 <= y + dx_dy_2[i][1] < 10:
            mass_1 = c[x + dx_dy_1[i][0]][y + dx_dy_1[i][1]]
            mass_2 = c[x + dx_dy_2[i][0]][y + dx_dy_2[i][1]]

        if mass_1 == 'x' and mass_2 == 'o':
            c[x + dx_dy_1[i][0]][y + dx_dy_1[i][1]] = '#'
            flag = True

    if flag:
        print('YES')
        sys.exit()

    dfs(x + 1, y)  # これだとxがした方向、yが右方向
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)


cnt = 0
for i in range(10):
    for j in range(10):
        if c[i][j] == 'o':
            cnt += 1
            dfs(i, j)

            break

if cnt == 1:
    print('YES')
    sys.exit()

print('NO')
