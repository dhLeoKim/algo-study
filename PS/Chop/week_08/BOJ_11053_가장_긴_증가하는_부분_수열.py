from sys import stdin

stdin = open("input/BOJ_11053_가장_긴_증가하는_부분_수열.txt")

N = int(stdin.readline().rstrip())
arr = list(map(int, stdin.readline().rstrip().split()))
memo = [0] * (max(arr)+1)

for n in arr:
    temp = max(memo[:n])
    memo[n] = max(memo[n], temp+1)
                
print(max(memo))