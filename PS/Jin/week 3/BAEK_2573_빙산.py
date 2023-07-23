# pypy3으로 제출

from collections import deque
import copy

N, M = list(map(int, input().split()))
iceberg = [list(map(int, input().split())) for _ in range(N)]
visited = [[[] for _ in range(M)] for _ in range(N)]
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

times = 0
while True:
    q = deque()
    # 빙산 확인 및 visited 업데이트
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] != 0:
                q.append([i, j])
                visited[i][j] = -1
            else:
                visited[i][j] = 0

    # 빙산이 다 녹은 경우
    if not q:
        print(0)
        break

    # 빙하 녹이기
    qq = deque()

    # 현재 바닷물인 것만 적용하기 위함
    iiceberg = copy.deepcopy(iceberg)

    # 맨 처음 값만 append
    for i, j in q:
        if iceberg[i][j] != 0:
            qq.append([i, j])
            visited[i][j] = 1
            break

    cnt = 0
    while qq:
        i, j = qq.popleft()
        cnt += 1
        for di, dj in d:
            if 0 <= i + di < N and 0 <= j + dj < M:
                if iiceberg[i+di][j+dj] == 0:
                    if iceberg[i][j] > 0:
                        iceberg[i][j] -= 1
                else:
                    if visited[i+di][j+dj] == -1:
                        visited[i+di][j+dj] = 1
                        qq.append([i+di, j+dj])
    else:
        if len(q) != cnt:
            print(times)
            break
        else:
            times += 1