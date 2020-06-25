n = input()
a, b, c, d = int(n[0]), int(n[1]), int(n[2]), int(n[3])

if a + b + c + d == 7:
    print('%d+%d+%d+%d=7' % (a, b, c, d))
elif a + b + c - d == 7:
    print('%d+%d+%d-%d=7' % (a, b, c, d))
elif a + b - c + d == 7:
    print('%d+%d-%d+%d=7' % (a, b, c, d))
elif a + b - c - d == 7:
    print('%d+%d-%d-%d=7' % (a, b, c, d))
elif a - b + c + d == 7:
    print('%d-%d+%d+%d=7' % (a, b, c, d))
elif a - b + c - d == 7:
    print('%d-%d+%d-%d=7' % (a, b, c, d))
elif a - b - c + d == 7:
    print('%d-%d-%d+%d=7' % (a, b, c, d))
else:
    print('%d-%d-%d-%d=7' % (a, b, c, d))

# 別解
a, b, c, d = list(input())
sign = "+-"
for i in range(2):  # 1つ目の記号
    for j in range(2):  # 2つ目の記号
        for k in range(2):  # 3つ目の記号
            if eval(a+sign[i]+b+sign[j]+c+sign[k]+d) == 7:
                print(str(a+sign[i]+b+sign[j]+c+sign[k]+d)+"=7")

# evalはpythonの構文で問題がなければそれを実行する
