import sys
sys.stdin = open('input_4485.txt')
input = sys.stdin.readline

from heapq import heappush, heappop

def dijkstra():
    h = []
    heappush(h, (lst[0][0], 0, 0))

    while h:
        cost_now, i, j = heappop(h)

        if d[i][j] < cost_now:
            continue

        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                cost_nxt = lst[ni][nj] + cost_now
                if cost_nxt < d[ni][nj]:
                    d[ni][nj] = cost_nxt
                    heappush(h, (cost_nxt, ni, nj))


INF = 1E9
di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
tc = 1

N = int(input())
while N != 0:
    lst = [list(map(int, input().split())) for _ in range(N)]
    d = [[INF]*N for _ in range(N)]

    dijkstra()
    ret = d[N-1][N-1]
    print(f'Problem {tc}:', ret)

    tc += 1
    N = int(input())