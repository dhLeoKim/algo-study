import sys
sys.stdin = open('input_17471.txt')
input = sys.stdin.readline

from collections import deque

def dfs(num):
    global ret

    if num == N+1:
        L = len(districtA)
        if L != 0 and L != N:
            totalA = bfs(districtA)
            totalB = bfs(districtB)
            
            if totalA != -1 and totalB != -1:
                diff = abs(totalA - totalB)
                if diff < ret:
                    ret = diff
        return
    
    districtA.append(num)
    dfs(num+1)
    districtA.pop()
    districtB.append(num)
    dfs(num+1)
    districtB.pop()


def bfs(district):
    queue = deque()
    queue.append(district[0])
    visited = [False]*(N+1)
    visited[district[0]] = True

    while queue:
        now = queue.popleft()
        for nxt in lst[now]:
            if not visited[nxt] and nxt in district:
                queue.append(nxt)
                visited[nxt] = True

    total = 0
    for i in district:
        total += population[i]
        if not visited[i]:
            return -1
    else:
        return total


N = int(input())
population = [0] + list(map(int, input().split()))
lst = [[]]
for _ in range(N):
    temp = list(map(int, input().split()))
    lst.append(temp[1:])

# 1. 두 선거구로 나누기
# 2. 나누는 것이 가능한지 확인
# 3. 나눠진 선거구 인구수 차이 갱신
# 4. 나누는것이 불가능할 경우 -1

ret = 1e9
districtA = []
districtB = []
chk = [False]*(N+1)
dfs(1)

if ret == 1e9:
    ret = -1

print(ret)