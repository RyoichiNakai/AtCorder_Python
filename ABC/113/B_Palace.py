n = int(input())
t, a = map(int, input().split())
height = [int(_) for _ in input().split()]
array = []
for i in range(n):
    array.append(abs((t - height[i] * 0.006) - a))

print(array.index(min(array)) + 1)
