from sys import stdin

stdin = open("input/BOJ_11660_구간_합_구하기_5.txt")

N, M = map(int, stdin.readline().rstrip().split())
graph = [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)]
area = [list(map(int, stdin.readline().rstrip().split()) for _ in range(M))]

for a in area:
    print(a)