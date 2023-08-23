from sys import stdin

stdin = open("input/BOJ_1931_회의실_배정.txt")

N = int(stdin.readline().rstrip())
table = [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)]
table.sort(key=lambda x: (x[1], x[0]))
cnt = 0
temp_end = 0

for t in table:
    if temp_end <= t[0]:
        temp_end = t[1]
        cnt += 1

print(cnt)
