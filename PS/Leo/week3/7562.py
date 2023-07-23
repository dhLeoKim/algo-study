import sys
sys.stdin = open('input_7562.txt')
input = sys.stdin.readline

from collections import deque

def bfs(start, end):
    queue = deque()
    queue.append((start[0], start[1]))
    board[start[0]][start[1]] = 0
    
    di, dj = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]

    if start == end:
        return 0

    while queue:
        i, j= queue.popleft()
        for k in range(8):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < L and 0 <= nj < L and board[ni][nj] == -1:
                if ni == end[0] and nj == end[1]:
                    return board[i][j] + 1
                board[ni][nj] = board[i][j] + 1
                queue.append((ni, nj))
                

T = int(input())
for tc in range(1, T+1):
    L = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    board = [[-1]*L for _ in range(L)]

    ret = bfs(start, end)
    print(ret)