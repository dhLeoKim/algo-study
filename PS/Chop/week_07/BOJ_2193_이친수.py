from sys import stdin

stdin = open("input/BOJ_2193_이친수.txt")

N = int(stdin.readline().rstrip())

memo = [0] * (N+2)
memo[1] = 1
memo[2] = 1

for i in range(3, N+1):
    memo[i] = memo[i-1] + memo[i-2]

print(memo[N])
