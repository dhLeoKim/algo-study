from sys import stdin

stdin = open("input/BAEK_1149_RGB_거리.txt")

N = int(stdin.readline().rstrip())
memo = [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)]

for i in range(1, N):
    # 각 색깔을 선택했을 때 얻을 수 있는 최소 누적 비용 계산
    memo[i][0] += min(memo[i-1][1], memo[i-1][2])
    memo[i][1] += min(memo[i-1][0], memo[i-1][2])
    memo[i][2] += min(memo[i-1][0], memo[i-1][1])
    
print(min(memo[-1]))