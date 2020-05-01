S = input()

S = S.replace("eraser", "0")
S = S.replace("erase", "0")
S = S.replace("dreamer", "0")
S = S.replace("dream", "0")
S = S.replace("0", "")

print("YES" if S == "" else "NO")

# 別解
# S = S[::-1]  # 文字列反転
