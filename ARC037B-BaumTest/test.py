import collections


def dfs(graph, start):
    stack = [start]
    visited = []
    cnt = 0
    while stack:
        label = stack.pop(0)
        if label not in visited:
            visited.append(label)
            stack = graph.get(label) + stack
        if __has_duplicates(stack):
            cnt = 1
    return visited, cnt


def __has_duplicates(seq):
    seen = []
    unique_list = [x for x in seq if x not in seen and not seen.append(x)]
    return len(seq) != len(unique_list)


n, m = map(int, input().split())
tree = collections.defaultdict(list)

for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    tree[u].append(v)
    tree[v].append(u)

# if len(list(tree)) != n:

print(list(tree), dict(tree))
num = 0
res = 0
while True:
    res += 1
    visited, cnt = dfs(dict(tree), num)
    res -= cnt

    if visited[-1] == list(tree)[-1]:
        break

    if visited[-1] + 1 <= list(tree)[-1]:
        num = visited[-1] + 1

print(res)



