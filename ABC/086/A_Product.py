import sys

s = input()
cnt = 0
if s[0] == '1':
    cnt += 1
if s[1] == '1':
    cnt += 1
if s[2] == '1':
    cnt += 1
print(cnt)

# 別解
# print(input().count('1'))

# 解説
# count関数は特定の文字列を含んでいるとカウントする
