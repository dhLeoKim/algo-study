from sys import stdin

stdin = open("input/BOJ_2217_로프.txt")

N = int(stdin.readline().rstrip())
ropes = [int(stdin.readline().rstrip()) for _ in range(N)]
ropes.sort(reverse=True)

ropes = [(idx+1)*r for idx, r in enumerate(ropes)]

print(max(ropes))
