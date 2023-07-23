from sys import stdin
from itertools import combinations

stdin = open("input\BAEK_1182_부분수열의_합.txt")

n, s = map(int, stdin.readline().rstrip().split())
arr = list(map(int, stdin.readline().rstrip().split()))
cnt = 0
for i in range(1, n+1):
    comb = combinations(arr, i)

    for x in comb:
        if sum(x) == s:
            cnt += 1

print(cnt)