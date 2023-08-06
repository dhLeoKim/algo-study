from collections import deque

N = int(input())
deq = deque(i+1 for i in range(N))

while len(deq) > 1:
    deq.popleft()
    a = deq.popleft()
    deq.append(a)
print(deq[0])