from sys import stdin

stdin = open("input/BOJ_10942_팰린드롬.txt")

N = int(stdin.readline().rstrip())
nums = [0] + list(map(int, stdin.readline().rstrip().split()))
M = int(stdin.readline().rstrip())
questions = [tuple(map(int, stdin.readline().rstrip().split())) for _ in range(M)]

memo = [[1]*(N+1) for _ in range(N+1)]

for r in range(N):
    for s in range(1, N+1):
        if s+1 <= N and s+r-1 <= N:
            if nums[s] != nums[s+r] or memo[s+1][s+r-1] == 0:
                memo[s][s+r] = 0

for q in questions:
    print(memo[q[0]][q[1]])