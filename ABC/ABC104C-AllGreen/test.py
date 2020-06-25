from itertools import product

d, g = map(int, input().split())
prob = []
for i in range(1, d + 1):
    p, c = map(int, input().split())
    prob.append((i * 100, p, c))  # score, num, bonus

ans = 10000000000000
for prd in product([0, 1], repeat=d):
    cnt = 0
    allScore = 0
    for j, (score, num, bonus) in zip(prd, prob):
        if j == 1:
            cnt += num
            allScore += score * num + bonus

    if allScore < g:
        for j, (score, num, bonus) in zip(prd, prob):
            # allScoreを更新しつつボーナスをつけないように調整
            # (score * num >= g - allScore)
            # これがないとその難易度の問題の得点において目標点数に到達できない問題数だったとしても
            # 目標点数に問題数を無視して到達することができてしまう
            if j == 0 and (score * num >= g - allScore):
                rest = (g - allScore) // score
                cnt += rest
                allScore += score * rest
                break

    if allScore >= g:
        ans = min(ans, cnt)

print(ans)
