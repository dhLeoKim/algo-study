import sys
sys.stdin = open('input_11053.txt')
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

# dp테이블 : i번째까지의 숫자로 만들 수 있는 가장 긴 부분 수열의 길이
# i번째의 값으로 만들 수 있는 증가하는 수열들 중에서
# 현재까지 가장 긴 수열에 +1

dp = [1] * N

for i in range(1, N):
    for j in range(i): 
        # lst[i]가 lst[j]보다 크다면, 즉 부분적으로 증가한다면
        if lst[j] < lst[i]: 
            # i에서의 최적의 해를 갱신, 기존의 수열에 lst[i]를 추가해서 +1 길이 가능
            dp[i] = max(dp[i], dp[j] + 1) 

print(max(dp))