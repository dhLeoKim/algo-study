# 시작점을 하나로만 계산하는 것이 아니라
# 가능한 모든 경우에 대한 최소값을 구해야 함

N = int(input())
paintC = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    paintC[i][0] += min(paintC[i-1][1], paintC[i-1][2])
    paintC[i][1] += min(paintC[i-1][0], paintC[i-1][2])
    paintC[i][2] += min(paintC[i-1][0], paintC[i-1][1])

print(min(paintC[N-1]))