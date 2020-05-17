# 無理だこれ
A, B, C, D, E, F = map(int, input().split())

w_list = []
s_list = []
d_list = []

for a in range(31):
    for b in range(31):
        for c in range(101):
            for d in range(101):
                w = (100 * A) * a + (100 * B) * b
                s = C * c + D * d
                if w == 0 or w + s > F:
                    break
                else:
                    if w // 100 * E >= s:
                        d = s / (w + s)
                        w_list.append(w)
                        s_list.append(s)
                        d_list.append(d)

print(w_list[d_list.index(max(d_list))] + s_list[d_list.index(max(d_list))], s_list[d_list.index(max(d_list))])


