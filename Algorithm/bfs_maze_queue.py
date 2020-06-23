from collections import deque


def bfs():
    # yが下方向，xが右方向
    d = [[float("inf")] * c for _ in range(r)]

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    que = deque([])
    que.append((sy, sx))
    d[sy][sx] = 0

    while que:
        print("que: {}".format(que), end='\n')

        p = que.popleft()

        print("p: {}".format(p), end='\n')
        for i in range(r):  # スタート位置
            for j in range(c):
                print(d[i][j], end=' ')
            print()
        print()

        if p[0] == gy and p[1] == gx:
            break
        for i in range(4):
            ny = p[0] + dy[i]
            nx = p[1] + dx[i]

            if 0 <= ny < r and 0 <= nx < c and maze[ny][nx] != "#" and d[ny][nx] == float("inf"):
                que.append((ny, nx))
                d[ny][nx] = d[p[0]][p[1]] + 1

    return d[gy][gx]


r, c = map(int, input().split())
sy, sx = map(lambda x: int(x) - 1, input().split())
gy, gx = map(lambda x: int(x) - 1, input().split())
maze = [list(input()) for i in range(r)]

print(bfs())


"""
bfsは同じ距離のものを見ながら進めていく！
入力

7 8
2 2
4 5
########
#......#
#.######
#..#...#
#..##..#
##.....#
########

"""