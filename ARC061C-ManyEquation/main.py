s = input()
res_list = []
# 2^nはbit全探索が効果絶大！！
for i in range(2 ** (len(s) - 1)):
    res = s[0]
    for j in range((len(s) - 1)):
        if (i >> j) & 1:
            res += '+'
        res += s[j + 1]
    res_list.append(eval(res))

print(sum(res_list))
