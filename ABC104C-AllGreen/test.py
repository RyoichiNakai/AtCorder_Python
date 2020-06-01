from itertools import product

d, g = map(int, input().split())
prob = []
for i in range(1, d + 1):
    p, c = map(int, input().split())
    prob.append((i * 100, p, c))  # score, num, bonus

print(prob)

# repeatは
for prd in product([0, 1], repeat=d):
    print(prd)


x = [5, 7, 2, 12]
y = [0, 1]
a = []
# zipの使い方
# forの引数が1つの場合:zipリストの同じインデックスの値を組み合わせたリストができる
# forの引数が2つの場合:それぞれの値を参照することができる
# forの引数が3つ以上の場合:エラー
# 長さが別のリストの場合:一番短いリストに合わされる

for x, y in zip(x, y):
    a.append(x)
    a.append(y)
print(a)
