from sys import stdin

stdin = open("input/BOJ_2239_스도쿠.txt")

sudoku = [list(map(int, stdin.readline().rstrip())) for _ in range(9)]
ans = []
