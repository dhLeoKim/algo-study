from sys import stdin

stdin = open("input/BOJ_9251_LCS.txt")

str_a = [0] + list(stdin.readline().rstrip())
str_b = [0] + list(stdin.readline().rstrip())
memo = [[0] * len(str_b) for _ in range(len(str_a))]

for i in range(1, len(str_a)):
    for j in range(1, len(str_b)):
        if str_a[i] == str_b[j]:
            memo[i][j] = memo[i-1][j-1] + 1
        else:
            memo[i][j] = max(memo[i-1][j], memo[i][j-1])

print(memo[-1][-1])