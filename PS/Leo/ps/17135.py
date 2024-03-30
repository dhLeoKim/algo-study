import sys
sys.stdin = open('input_17135.txt')
input = sys.stdin.readline

from collections import deque

def bfs(archer_pos):
    queue = deque()
    queue.append(archer_pos)

    while queue:
        i, j, d = queue.popleft()
        if d > D:
            continue
        for k in range(3):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if board[ni][nj] == 1:
                    enemy.add((ni, nj))
                    board_temp[ni][nj] = 0
                    return
                else:
                    queue.append((ni, nj, d+1))


def playCastleDefence(archer):
    global board, board_temp, enemy

    board = []
    for row in lst:
        board.append(row[:])

    cnt = 0
    for _ in range(N):
        board_temp = []
        for row in board:
            board_temp.append(row[:])

        enemy = set()
        for idx in range(3):
            bfs(archer[idx])
        
        cnt += len(enemy)
        board_temp.pop()
        board = [[0]*M]
        for row in board_temp:
            board.append(row[:])

    return cnt


def dfs(depth, idx):
    global ret

    if depth == 3:
        cnt = playCastleDefence(archer)
        ret = max(ret, cnt)
        return

    for j in range(idx, M):
        archer.append((N, j, 1))
        dfs(depth+1, j+1)
        archer.pop()


N, M, D = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

di, dj = [0, -1, 0], [-1, 0, 1]
archer = []
ret = 0
dfs(0, 0)

print(ret)