N = int(input())
A = list(map(int, input().split()))
cnt = 0

# all(): 全ての要素がTrueならTrue
# any(): 一つでもTrueならTrue
while all(a % 2 == 0 for a in A):
    A = [a/2 for a in A]
    cnt += 1

print(cnt)

# 別解
# n = int(input())
# a = list(map(int, input().split()))

# ans = float("inf")

# for i in a:
#    ans = min(ans, len(bin(i)) - bin(i).rfind("1") - 1) # (1)…2で割った回数が最小のものを探索
# print(ans)


