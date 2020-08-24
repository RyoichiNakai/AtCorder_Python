from collections import deque


def dfs(sy, sx, gy, gx):
    # yが下方向，xが右方向
    # 今回は到達できるかどうかなので，Booleanを使用
    # 壁を何回壊すと進入可能なのかが必要となるため，リストの次数を1つあげる
    d = [[[False] * 3 for _ in range(w)] for _ in range(h)]

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    que = deque([])
    que.append((sy, sx, 0))
    d[sy][sx][0] = True

    while que:
        # bfsでとくと，時間が間に合わないことからdfsでとく
        # なので，popleftからpopに変更してstackを用いる
        p = que.pop()

        if p[0] == gy and p[1] == gx:
            break

        for i in range(4):
            ny = p[0] + dy[i]
            nx = p[1] + dx[i]
            cnt = p[2]

            if 0 <= ny < h and 0 <= nx < w and not d[ny][nx][cnt]:
                if maze[ny][nx] != "#":
                    que.append((ny, nx, cnt))
                elif cnt < 2 and maze[ny][nx] == "#":
                    que.append((ny, nx, cnt + 1))
                d[ny][nx][cnt] = True

    for i in range(3):
        if d[gy][gx][i]:
            return True


h, w = map(int, input().split())
maze = [list(input()) for _ in range(h)]
sy, sx, gy, gx = 0, 0, 0, 0

for i in range(h):
    for j in range(w):
        if maze[i][j] == "s":
            sy = i
            sx = j
        if maze[i][j] == "g":
            gy = i
            gx = j

if dfs(sy, sx, gy, gx):
    print("YES")
else:
    print("NO")
