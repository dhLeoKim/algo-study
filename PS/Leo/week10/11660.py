import sys
sys.stdin = open('input_11660.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

prefix_sum = [[0]*N for _ in range(N)]