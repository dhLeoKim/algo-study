import sys

dd = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
diag = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
N, M = map(int, sys.stdin.readline().strip().split())
basket = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

# 구름 이동
def moving_clouds(clouds, d, s):
    # 구름 이동 및 비
    di, dj = dd[d-1]
    moved_clouds = [[0] * N for _ in range(N)]
    for cloud in clouds:
        basket[(cloud[0] + di*s) % N][(cloud[1] + dj*s) % N] += 1
        moved_clouds[(cloud[0]+di*s) % N][(cloud[1]+dj*s) % N] = 1
    # 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니 수만큼 물 증가
    for i in range(N):
        for j in range(N):
            if moved_clouds[i][j] == 1:
                for diai, diaj in diag:
                    if 0 <= i + diai < N and 0 <= j + diaj < N:
                        if basket[i + diai][j + diaj] > 0:
                            basket[i][j] += 1
    # 구름 생성
    new_clouds = []
    for i in range(N):
        for j in range(N):
            if basket[i][j] >= 2:
                if moved_clouds[i][j] == 0:
                    basket[i][j] -= 2
                    new_clouds.append([i, j])
    return new_clouds


# 이동 정보
clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
for _ in range(M):
    d, s = map(int, sys.stdin.readline().strip().split())
    clouds = moving_clouds(clouds, d, s)

# 바구니 전체 물 양
total = 0
for i in range(N):
    total += sum(basket[i])
print(total)