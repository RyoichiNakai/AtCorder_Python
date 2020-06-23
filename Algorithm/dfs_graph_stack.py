def dfs(graph, start, end):
    stack = [start]
    visited = []
    while stack:
        label = stack.pop(0)
        if label == end:
            visited.append(label)
            __logging(visited, stack)
            return visited
        if label not in visited:
            visited.append(label)
            stack = graph.get(label, []) + stack
            # graph.getは第1引数が辞書のキーで第２引数がそのキーがなかったときに[]を返すという意味
        __logging(visited, stack)
    return visited


def __logging(visited, stack):
    if stack:
        print("visited: {}".format(visited), end="\n")
        print("stack: {}".format(stack), end="\n")
    else:
        print("visited: {}".format(visited), end="\n")


"""
dfsは1つのものを深く見ていく！
+-------------1
|             |
|     +-------+-----+
|     |       |     |
|   +-2-+     6   +-8-+
|   |   |     |   |   |
|   3   4     7   9   10
|       |     |   |   |
+-------5     +---+   11
"""


graph = {1: [2, 6, 8],
         2: [3, 4],
         3: [],
         4: [5],
         5: [1],
         6: [7],
         7: [],
         8: [9, 10],
         9: [7],
         10: [11],
         11: []}


dfs(graph, 1, 11)
