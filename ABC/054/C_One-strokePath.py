"""
from collections import defaultdict


def dfs(start, visited):
    if len(visited) == n:
        ans.append(visited)
    else:
        for c in graph[start]:
            if c not in visited:
                dfs(c, visited + [c])


n, m = map(int, input().split())
tree = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

graph = dict(tree)
ans = []
dfs(1, [1])
print(len(ans))
print(ans)

"""

"""
import itertools

n, m = map(int, input().split())

path = [[False] * n for _ in range(n)]

# 無向グラフを解く時の頂点と辺の関係をTrue/Falseで表す
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    path[a][b] = True
    path[b][a] = True

# print(path)

ans = 0

# 頂点を並び替える順列を生成してループ
for i in itertools.permutations(range(n), n):
    # print(i)
    # 頂点1が始点
    if i[0] == 0:
        # 生成した順列の中をさらにループ
        for j in range(n):
            # n - 1 まで続いたら条件を満たすパスが存在する(なんで?)
            if j == n - 1:
                ans += 1
                break
            # i[j] から i[j + 1] にいくパスがなければ終了
            if not path[i[j]][i[j + 1]]:
                break

print(ans)
"""

# ダメだったやつ
from collections import defaultdict


def dfs(graph, start):
    stack = list()
    ans = 0
    f_vertex = graph.get(start)  # 始点と隣接しているノード

    # 1とつながっている頂点の数だけfor文を回す
    for child in f_vertex:
        stack.append(child)  # dfsしたいノードをstackにappend
        visited = [start]  # visitedをリセット

        # stackの分だけループを回す
        while stack:
            node = stack.pop(0)

            if node not in visited and node in graph[visited[-1]]:
                visited.append(node)  # 訪問済のノードを追加
                stack = graph.get(node) + stack  # 子ノードをstackに追加

        if len(visited) == n:
            ans += 1

    return ans


n, m = map(int, input().split())
tree = defaultdict(list)


# 隣接関係をdict型に保存
for _ in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 今回は始点が1と決まっているためにstartの位置を1と設定
print(dfs(dict(tree), 1))
