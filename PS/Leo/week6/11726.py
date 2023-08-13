import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*1002

# dp[i] 는 i번째까지 직사각형을 채우는 방법의 수

# 초기값
dp[1] = 1
dp[2] = 2

# i번째까지 채우는 방법은 
# 1. i-1번까지의 방법 + 1칸 채우기
# 2. i-2번까지의 방법 + 2칸 채우기
for i in range(3, 1001):
    dp[i] = dp[i-1] + dp[i-2]   

print(dp[n]%10007)