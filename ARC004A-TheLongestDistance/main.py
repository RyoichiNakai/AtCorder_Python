from itertools import combinations
import math


def get_distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d


n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
index = [i for i in range(n)]
comb = list(combinations(index, 2))
dis_list = []
print(n, xy, index, comb)

for c in comb:
    x_1 = xy[c[0]][0]
    x_2 = xy[c[1]][0]
    y_1 = xy[c[0]][1]
    y_2 = xy[c[1]][1]
    dis_list.append((get_distance(x_1, y_1, x_2, y_2)))

print(min(dis_list))
