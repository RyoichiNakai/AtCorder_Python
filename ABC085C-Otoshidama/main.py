N, Y = map(int, input().split())

for m10 in range(N + 1):
    for m5 in range(N + 1 - m10):
        m1 = N - m10 - m5
        if m10 * 10000 + m5 * 5000 + m1 * 1000 == Y:
            print(m10, m5, m1)
            exit(0)

print('-1 -1 -1')
