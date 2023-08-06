import sys
input = sys.stdin.readline

# 원판 N개를 a번 기둥에서 b번 기둥으로 옮기는 함수
# 1. N-1개의 원판을 기둥 a에서 기둥 6-a-b로 옮긴다.
# 2. N번째의 원판을 기둥 a에서 기둥 b로 옮긴다.
# 3. N-1개의 원판을 기둥 6-a-b에서 기둥 b로 옮긴다.

def hanoi(a, b, N):
    if N == 1:
        print(a, b)
        return
    
    hanoi(a, 6-a-b, N-1)
    print(a, b)
    hanoi(6-a-b, b, N-1)


N = int(input())
print(2**N - 1)
hanoi(1, 3, N)