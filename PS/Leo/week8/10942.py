import sys
sys.stdin = open('input_10942.txt')
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

dp = [[0]*N for _ in range(N)]

# 한글자
for i in range(N):              
    dp[i][i] = 1

# 두글자
for i in range(N-1):            
    if lst[i] == lst[i+1]:
        dp[i][i+1] = 1

# 세글자 이상
for gap in range(2, N):         
    for i in range(N-gap):
        # 양끝의 단어가 같고, 이전까지가 팰린드롬이면 => 팰린드롬이다!
        if lst[i] == lst[i+gap] and dp[i+1][i+gap-1] == 1:  
            dp[i][i+gap] = 1                                

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S-1][E-1])
