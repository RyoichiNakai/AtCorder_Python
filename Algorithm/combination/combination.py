import itertools
# 組み合わせ
# combinations(list, n) で list から n 個選ぶ
for i in itertools.combinations([0, 1, 2], 2):
    print(i)
# (0, 1)
# (0, 2)
# (1, 2)
