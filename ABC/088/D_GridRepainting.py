from collections import deque


def bfs(sy, sx, gy, gx):
    # yが下方向，xが右方向
    d = [[float("inf")] * w for _ in range(h)]

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    que = deque([])
    que.append((sy, sx))
    d[sy][sx] = 0

    while que:

        p = que.popleft()

        if p[0] == gy and p[1] == gx:
            break

        for i in range(4):
            ny = p[0] + dy[i]
            nx = p[1] + dx[i]

            if 0 <= ny < h and 0 <= nx < w and maze[ny][nx] != "#" and d[ny][nx] == float("inf"):
                que.append((ny, nx))
                d[ny][nx] = d[p[0]][p[1]] + 1

    if d[gy][gx] == float("inf"):
        return -1
    else:
        return d[gy][gx]


h, w = map(int, input().split())
maze = [list(input()) for _ in range(h)]

res = 0
for y in range(h):
    for x in range(w):
        if maze[y][x] == '#':
            res += 1

dis = bfs(0, 0, h - 1, w - 1)

if dis == -1:
    print(-1)
else:
    print(h * w - res - dis - 1)
