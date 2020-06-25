import collections
# 該当する頂点がないことを示す値
INVALID = -1

n, m = map(int, input().split())
tree = collections.defaultdict(list)


def bfs(u):
    queue = collections.deque([u])
    d = [None] * n  # uからの距離の初期化
    d[u] = 0  # 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in tree[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d


for _ in range(m):
    # 入力は1始まりであるので、これを0始まりに変換する
    u, v = map(lambda x: int(x) - 1, input().split())
    # tree[？]はキーになっており、appendすることで木の接続関係を保存することができる
    tree[u].append(v)
    tree[v].append(u)

d = bfs(tree)
print(list(tree), dict(tree))
