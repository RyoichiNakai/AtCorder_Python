from itertools import combinations
import math

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
index = [_ for _ in range(n)]
comb = list(combinations(index, 2))
dis_list = []

for c in comb:
    x1 = xy[c[0]][0]
    x2 = xy[c[1]][0]
    y1 = xy[c[0]][1]
    y2 = xy[c[1]][1]
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    dis_list.append(round(d, 6))

print(max(dis_list))
