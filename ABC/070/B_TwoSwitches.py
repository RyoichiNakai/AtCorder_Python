a, b, c, d = map(int, input().split())
alice = [_ for _ in range(a, b + 1)]
bob = [_ for _ in range(c, d + 1)]
dt = list(set(alice) & set(bob))
print(dt[-1] - dt[0] if dt != [] else 0)

# 別解
"""
a_c = max(a,c)
b_d = min(b,d)
dum = b_d - a_c
if dum < 0:
    print(0)
else:
    print(dum)
"""
