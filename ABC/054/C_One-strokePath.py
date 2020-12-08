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
