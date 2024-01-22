import sys
sys.stdin = open('input_13335.txt')
input = sys.stdin.readline

from collections import deque

N, W, L = map(int, input().split())
lst = deque(map(int, input().split()))

time = 0
bridge = deque([0]*W)
while bridge:
    time += 1
    bridge.popleft()		

    if lst:
        if sum(bridge) + lst[0] <= L:
            bridge.append(lst.popleft())
        else:
            bridge.append(0)

print(time)