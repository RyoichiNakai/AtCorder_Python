from itertools import product

# repeatの回数まで0と1の組み合わせを表示してくれる
for prd in product([0, 1], repeat=4):
    print(prd)

# 結果
# 4であれば(0,0,0,0)から(1,1,1,1)までの0と1の組み合わせを表示してくれる
