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
ダメだったやつ
import collections


def dfs(graph, start, num):
    ans = 0
    stack = list()
    f_vertex = graph.get(start)  # 始点と隣接しているノード
    print(graph)

    # 1とつながっている頂点の数だけfor文を回す
    for child in f_vertex:
        stack.append(child)  # dfsしたいノードをstackにappend
        visited = [start]  # visitedをリセット

        # stackの分だけループを回す
        while stack:
            node = stack.pop(0)
            print("node:{}".format(node))
            if node not in visited:
                visited.append(node)  # 訪問済のノードを追加
                print("visited:{}".format(visited))
                stack = graph.get(node) + stack  # 子ノードをstackに追加
                print("stack:{}".format(stack))

        if len(visited) == num:
            ans += 1
            print("ans:{}".format(ans))

    return ans


n, m = map(int, input().split())
tree = collections.defaultdict(list)

# 隣接関係をdict型に保存
for _ in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 今回は始点が1と決まっているためにstartの位置を1と設定
print(dfs(dict(tree), 1, m))

"""