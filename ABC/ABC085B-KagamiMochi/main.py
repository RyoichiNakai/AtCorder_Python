N = int(input())
d = [int(input()) for _ in range(N)]
d.sort()
print(1 + sum(d[i] != d[i + 1] for i in range(N - 1)))

# 別解
# setは和集合
print(len(set(d)))

