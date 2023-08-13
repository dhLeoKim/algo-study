from sys import stdin

stdin = open("input/BOJ_11726_2×n_타일링.txt")

N = int(stdin.readline().rstrip())

memo = [0] * 1001
memo[1] = 1
memo[2] = 2

for i in range(3,1001):
  memo[i] = memo[i-1] + memo[i-2]

print(memo[N] % 10007)