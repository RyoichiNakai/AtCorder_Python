x = [5, 7, 2, 12]
y = [0, 1]
a = []

# zipの使い方
# forの引数が1つの場合:zipリストの同じインデックスの値を組み合わせたリスト(5,0)...ができる
# forの引数が2つの場合:それぞれの値を参照することができる(5,0,7,1)
# forの引数が3つ以上の場合:エラー
# 長さが別のリストの場合:一番短いリストに合わされる
# zipの中身はタプル(0,1...),リストではない

for x, y in zip(x, y):
    a.append(x)
    a.append(y)
print(a)
