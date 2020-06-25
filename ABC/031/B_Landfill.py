import sys
import copy

sys.setrecursionlimit(10 ** 8)  # 再帰関数の呼び出し制限
c = [list(input()) for i in range(10)]
c_copy = copy.deepcopy(c)


# つながっているところだけを探索する！
def dfs(x, y):
    if not (0 <= x < 10) or not (0 <= y < 10) or c_copy[x][y] == 'x':
        # 壁に当たったり、探索範囲外になった場合はreturn
        return

    c_copy[x][y] = "x"  # 探索済みの島のところを海にする

    dfs(x + 1, y)  # これだとxがした方向、yが右方向
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)


def checked():
    # 島が1つなればdfsで全体が海になる
    for i in range(10):
        for j in range(10):
            if c_copy[i][j] == 'o':
                return False
    return True


for i in range(10):
    for j in range(10):
        if c[i][j] == 'x':
            c_copy = copy.deepcopy(c)
            c_copy[i][j] = 'o'
            dfs(i, j)
            if checked():
                print('YES')
                exit(0)

print('NO')


# def dfs_o(x, y):
#     if not (0 <= x < 10) or not (0 <= y < 10) or c_o[x][y] == 'x' or c_o[x][y] == '#':  # 壁に当たったり、探索範囲外になった場合はreturn
#         return
#
#     c_o[x][y] = "#"  # 探索済みを示すためのマーキング
#
#     dfs_o(x + 1, y)  # これだとxがした方向、yが右方向
#     dfs_o(x - 1, y)
#     dfs_o(x, y + 1)
#     dfs_o(x, y - 1)
#
#
# def dfs_x(x, y):
#     if not (0 <= x < 10) or not (0 <= y < 10) or c_x[x][y] == 'o' or c_x[x][y] == '#':  # 壁に当たったり、探索範囲外になった場合はreturn
#         return
#
#     c_x[x][y] = "#"  # 探索済みを示すためのマーキング
#
#     dx = [1, -1]
#     dy = [1, -1]
#
#     if (1 <= x < 9) and (1 <= y < 9):
#         if (c_x[x + dx[0]][y] == 'o' and c_x[x + dx[1]][y] == 'o') or (c_x[x][y + dy[0]] == 'o' and c_x[x][y + dy[1]] == 'o'):
#             print('YES')
#             sys.exit()
#
#     dfs_x(x + 1, y)  # これだとxがした方向、yが右方向
#     dfs_x(x - 1, y)
#     dfs_x(x, y + 1)
#     dfs_x(x, y - 1)
#
#
# cnt = 0
# for i in range(10):
#     for j in range(10):
#         if c_o[i][j] == 'o':
#             cnt += 1
#             dfs_o(i, j)
#             break
#
# if cnt == 1:
#     print('YES')
#     sys.exit()
#
# for i in range(10):
#     for j in range(10):
#         if c_x[i][j] == 'x':
#             dfs_x(i, j)
#             break
#
# print('NO')
