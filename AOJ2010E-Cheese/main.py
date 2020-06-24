## bfsを使って動的にstartとgoalを変えればいい？？

from collections import deque


def bfs():
    # yが下方向，xが右方向
    d = [[float("inf")] * w for _ in range(h)]

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    que = deque([])
    # que.append((sy, sx))
    # d[sy][sx] = 0

    while que:
        print("que: {}".format(que), end='\n')

        p = que.popleft()

        # if p[0] == gy and p[1] == gx:
        #     break
        for i in range(4):
            ny = p[0] + dy[i]
            nx = p[1] + dx[i]

            if 0 <= ny < h and 0 <= nx < w and maze[ny][nx] != "#" and d[ny][nx] == float("inf"):
                que.append((ny, nx))
                d[ny][nx] = d[p[0]][p[1]] + 1

    return # d[gy][gx]


h, w, n = map(int, input().split())
num = [i + 1 for i in range(n)]
maze = [list(input()) for i in range(h)]

for i in range(h):
    for j in range(w):
        print()


print(h, w, n)