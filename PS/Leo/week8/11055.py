import sys
sys.stdin = open('input_11055.txt')
input = sys.stdin.readline

N = int(input())
lst = [0] + list(map(int, input().split()))

# dp테이블 : i번째까지의 숫자로 만들 수 있는 가장 큰 부분 수열의 합
# i번째의 값으로 만들 수 있는 증가하는 수열들 중에서
# 현재까지 합이 가장 큰 수열에 +lst[i]

dp = [0]*(N+1)

for i in range(1, N+1):
    temp = 0
    for j in range(0, i):
        if lst[i] > lst[j]:
            temp = max(temp, dp[j])
    dp[i] = temp + lst[i]

print(max(dp))