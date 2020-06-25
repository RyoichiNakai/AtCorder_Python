# 別解
# sortedはlist以外でも(iterableならok!)
s = sorted(input())
t = sorted(input())[::-1]  # reverse

if s < t:
    print('Yes')
else:
    print('No')

exit(0)

# 自分の回答
s = input()
s_list = [s[i] for i in range(len(s))]
t = input()
t_list = [t[i] for i in range(len(t))]
s_list.sort()
t_list.sort(reverse=True)
n = min(len(s), len(t))

for i in range(n):
    if s_list[i] < t_list[i]:
        print('Yes')
        exit(0)
    elif s_list[i] == t_list[i]:
        if i != n - 1:
            continue
        else:
            if len(s) >= len(t):
                print('No')
            else:
                print('Yes')
            exit(0)

    else:
        print('No')
        exit(0)




