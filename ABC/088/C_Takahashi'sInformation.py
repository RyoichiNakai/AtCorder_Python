c_1 = list(map(int, input().split()))
c_2 = list(map(int, input().split()))
c_3 = list(map(int, input().split()))
c = c_1 + c_2 + c_3
if sum(c) == 3 * (c_1[0] + c_2[1] + c_3[2]):
    print('Yes')
else:
    print('No')
