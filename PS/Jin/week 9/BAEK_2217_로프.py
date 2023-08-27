import sys

N = int(sys.stdin.readline().strip())

rope = []
for _ in range(N):
    rope.append(int(sys.stdin.readline().strip()))

rope.sort()
maxW = 0
for i in range(N):
    if maxW < rope[i] * (N-i):
        maxW = rope[i] * (N-i)
print(maxW)