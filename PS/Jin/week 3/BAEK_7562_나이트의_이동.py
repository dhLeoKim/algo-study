from collections import deque

k = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]

T = int(input())
for _ in range(T):
    l = int(input())
    chess = [[0] * l for _ in range(l)]
    visited = [[0] * l for _ in range(l)]
    cur = list(map(int, input().split()))
    des = list(map(int, input().split()))
    chess[cur[0]][cur[1]] = 'c'
    chess[des[0]][des[1]] = 'd'
    visited[cur[0]][cur[1]] = 1

    # bfs
    q = deque([cur])
    while q:
        a = q.popleft()
        if a == des:
            print(visited[a[0]][a[1]] - 1)
            break
        for i, j in k:
            # 이동 후 위치가 체스판 내에 있고 visited가 0인 경우
            if 0 <= a[0] + i < l and 0 <= a[1] + j < l and visited[a[0]+i][a[1]+j] == 0:
                visited[a[0]+i][a[1]+j] = visited[a[0]][a[1]] + 1
                q.append([a[0]+i, a[1]+j])