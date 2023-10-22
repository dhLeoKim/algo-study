from sys import stdin

stdin = open("input/BOJ_17141_연구소_2.txt")

N, M = map(int, stdin.readline().rstrip().split())
graph = [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)]

