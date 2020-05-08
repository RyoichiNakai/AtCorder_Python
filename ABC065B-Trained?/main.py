N = int(input())
d = [int(input()) for _ in range(N)]
cnt = 0
index = 1
for i in range(N):
    cnt += 1
    num = d[index - 1]
    print(num)
    if num == 2:
        print(cnt)
        exit(0)
    index = num
print(-1)
