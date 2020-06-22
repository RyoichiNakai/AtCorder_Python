import collections


def dfs(graph, start):
    stack = [start]
    flag = False
    global visited
    global cnt
    while stack:
        label = stack.pop(0)
        if label not in visited:
            visited.append(label)
            if graph.get(label) in stack:
                flag = True
            else:
                stack = graph.get(label) + stack
    if flag:
        cnt -= 1


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

cnt = 0
visited = []

for i in range(n):
    if i in visited:
        continue

    if i in list(tree):
        dfs(dict(tree), i)

    cnt += 1

print(cnt)



