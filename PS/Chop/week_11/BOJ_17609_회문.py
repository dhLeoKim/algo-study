from sys import stdin

stdin = open("input/BOJ_17609_회문.txt")

N = int(stdin.readline().rstrip())
words = [(['0'] + list(stdin.readline().rstrip().split())) for _ in range(N)]

memo = [[1]*(N+1) for _ in range(N+1)]

for r in range(N):
    for s in range(1, N+1):
        if s+1 <= N and s+r <= N:
            if words[s] != words[s+r] or memo[s+1][s+r-1] == 0:
                memo[s][s+r] = 0

print(memo[-1][-1])