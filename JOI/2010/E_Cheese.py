import collections


def bfs(sy, sx, gy, gx):
    # yが下方向，xが右方向
    d = [[float("inf")] * w for _ in range(h)]

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    que = collections.deque([])
    que.append((sy, sx))
    d[sy][sx] = 0

    while que:

        p = que.popleft()

        if p[0] == gy and p[1] == gx:
            break

        for k in range(4):
            ny = p[0] + dy[k]
            nx = p[1] + dx[k]

            if 0 <= ny < h and 0 <= nx < w and maze[ny][nx] != "X" and d[ny][nx] == float("inf"):
                que.append((ny, nx))
                d[ny][nx] = d[p[0]][p[1]] + 1

    return d[gy][gx]


h, w, n = map(int, input().split())
num = [_ for _ in range(1, n + 1)]
sg = collections.defaultdict(list)
maze = [list(input()) for _ in range(h)]
res = 0

for y in range(h):
    for x in range(w):

        if maze[y][x] == 'S':
            sg[0].append(y)
            sg[0].append(x)

        if maze[y][x] in str(num):
            sg[int(maze[y][x])].append(y)
            sg[int(maze[y][x])].append(x)

for i in range(n):
    res += bfs(sg[i][0], sg[i][1], sg[i + 1][0], sg[i + 1][1])

print(res)
