import collections


def dfs(graph, start, num):
    ans = 0
    stack = list()
    f_vertex = graph.get(start)

    # 1とつながっている頂点の数だけfor文を回す
    for child in f_vertex:
        # dfsしたいノードをstackにappend
        stack.append(child)
        # visitedには探索済のノードをリストとして保持
        visited = [start, child]
        # print("stack:{}".format(stack))

        # stackの分だけループを回す
        while stack:
            node = stack.pop()
            # print(graph.get(node))
            for c_node in graph.get(node):
                if c_node not in visited:
                    visited.append(c_node)  # 探索したノードを追加
                    # print("visited:{}".format(visited))
                    stack.append(c_node)
                    # print("stack:{}".format(stack))

        if len(visited) == num:
            ans += 1

    return ans


n, m = map(int, input().split())
# グラフ系の問題はこれを使うと便利
tree = collections.defaultdict(list)

# 隣接関係をdict型に保存
for _ in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 今回は始点が1と決まっているためにstartの位置を1と設定
print(dfs(dict(tree), 1, m))
