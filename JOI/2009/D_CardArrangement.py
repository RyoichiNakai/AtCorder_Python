import itertools

n = int(input())
k = int(input())

card = [int(input()) for _ in range(n)]

arrangement = list()

for i in itertools.permutations(card, k):
    num = ''
    for j in i:
        num += str(j)
    arrangement.append(int(num))

print(len(set(arrangement)))
