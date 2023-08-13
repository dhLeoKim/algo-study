import sys
from itertools import combinations
from collections import deque

# 조건1 : 7명
# 조건2 : S가 4명 이상
# 조건3 : bfs 확인

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs(i):
    global answer
    visited = [[0] * 5 for _ in range(5)]
    new = deque()
    new.append(i[0])
    while new:
        a, b = new.popleft()
        visited[a][b] = 1
        for di, dj in d:
            if 0 <= a+di < 5 and 0 <= b+dj < 5 and visited[a+di][b+dj] == 0 and loc[a+di][b+dj] == 1:
                visited[a+di][b+dj] = 1
                new.append([a+di, b+dj])
    else:
        if loc == visited:
            answer += 1


arr = []
for _ in range(5):
    arr.append(sys.stdin.readline().strip())

students = []
for num in range(25):
    r = num // 5
    c = num % 5
    students.append([r, c])

answer = 0
# 7명 뽑기
seven_students = combinations(students, 7)
for i in list(seven_students):
    # S가 4개 이상인지 확인
    cnt = 0
    loc = [[0] * 5 for _ in range(5)]
    for j in i:
        loc[j[0]][j[1]] = 1
        if arr[j[0]][j[1]] == 'Y':
            cnt += 1
            if cnt >= 4:
                break
    # 인접해있는지 확인
    else:
        # list로 변환하여 bfs
        bfs(i)

print(answer)