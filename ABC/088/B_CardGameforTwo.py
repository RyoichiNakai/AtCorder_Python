N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
Alice = sum(A[i] for i in range(0, N, 2))
Bob = sum(A[i] for i in range(1, N, 2))
print(Alice - Bob)

# 別解
print(sum(A[::2]) - sum(A[1::2]))


