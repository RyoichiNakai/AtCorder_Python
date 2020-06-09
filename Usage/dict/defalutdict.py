from collections import defaultdict

# 引数は無名関数(lamda)のようにクラスの型している
d = defaultdict(list)

# d[i]がキーとなっており、append(i)でキーのところにiを代入する
for i in range(10):
    d[i].append(i)

print(d)
