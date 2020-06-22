import collections


def dfs(graph, start):

    stack = [start]
    flag = False
    global visited
    global cnt

    while stack:
        label = stack.pop(0)

        # まだ訪れたことがなかったら，探索に追加
        if label not in visited:
            visited.append(label)
            # stackに現在のノードの子ノード値が含まれていると閉路になっている．
            for c_node in graph.get(label):
                if c_node in stack:
                    flag = True
            stack = graph.get(label) + stack

    if flag:
        cnt -= 1


# 問題の読み込み
n, m = map(int, input().split())
# グラフ系の問題はこれを使うと便利
tree = collections.defaultdict(list)

# 隣接関係をdict型に保存
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    tree[u].append(v)
    tree[v].append(u)

cnt = 0
visited = []

for i in range(n):

    # visitedに含まれる際はcontinueする
    if i in visited:
        continue

    if i in list(tree):
        dfs(dict(tree), i)

    cnt += 1

print(cnt)
