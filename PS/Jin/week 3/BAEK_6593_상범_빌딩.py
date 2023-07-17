from collections import deque

while True:
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        break

    # 데이터 받아오기
    visited = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)] # 얕은 복사 되지 않게 주의
    # print(visited)
    cur = [-1, -1, -1]
    des = [-1, -1, -1]
    for l in range(L):
        for r in range(R):
            floor = input()
            for c in range(C):
                if floor[c] == 'S':
                    cur = [l, r, c]
                    visited[l][r][c] = 1
                elif floor[c] == '.':
                    visited[l][r][c] = 0
                elif floor[c] == '#':
                    visited[l][r][c] = -1
                elif floor[c] == 'E':
                    des = [l, r, c]
        input()

    # bfs
    # 상하좌우앞뒤
    d = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]
    q = deque([cur])
    while q:
        i, j, k = q.popleft()
        if [i, j, k] == des:
            print('Escaped in', visited[i][j][k] - 1, 'minute(s).')
            break
        for da, db, dc in d:
            if 0 <= (i+da) < L and 0 <= (j+db) < R and 0 <= (k+dc) < C:
                if visited[i+da][j+db][k+dc] == 0:
                    visited[i+da][j+db][k+dc] = visited[i][j][k] + 1
                    q.append([i+da, j+db, k+dc])
    else:
        print('Trapped!')