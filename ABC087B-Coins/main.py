# A, B, C, X = map(int, open(0).read().split())
# 本番ではこれ使うといい
A = int(input())
B = int(input())
C = int(input())
X = int(input())
print(sum(i * 500 + j * 100 + k * 50 == X
          for i in range(A + 1) for j in range(B + 1) for k in range(C + 1)))
