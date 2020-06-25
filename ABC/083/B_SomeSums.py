# N, A, B = map(int, open(0).read().split())
N, A, B = map(int, input().split())
sub = 0

for i in range(1, N + 1):
    # 各桁の和を出す処理
    w = sum(list(map(int, str(i))))
    if A <= w & w <= B:
        sub += i

# 普通　実行時間:37ms 表記のバイト数:206byte
print(sub)
# リスト内包表記　実行時間:46ms 表記のバイト数:146byte
print(sum(i for i in range(1, N + 1) if A <= sum(list(map(int, str(i)))) & sum(list(map(int, str(i)))) <= B))
