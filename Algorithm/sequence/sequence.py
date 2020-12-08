import itertools


# 順列
# permutations(list, n) で list から n 個選んで並べる
for i in itertools.permutations([0, 1, 2], 3):
    print(i)
# (0, 1, 2)
# (0, 2, 1)
# (1, 0, 2)
# (1, 2, 0)
# (2, 0, 1)
# (2, 1, 0)
