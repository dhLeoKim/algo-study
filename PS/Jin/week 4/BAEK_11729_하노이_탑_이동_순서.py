import sys

N = int(sys.stdin.readline().strip())

# hanoi(횟수, 시작점, 끝점)
# 전체 번호 1+2+3=6에서 시작점과 끝점을 뺀 값이 나머지 장대
def hanoi(N, start, end):
    if N == 1:
        print(start, end)
        return
    # 제일 큰 원판을 제외한 나머지를 시작점에서 끝점이 아닌 다른 점으로 옮기기
    hanoi(N-1, start, 6-start-end)
    # 제일 큰 원판 시작점에서 끝 점으로 옮기기
    print(start, end)
    # 다시 그 상태에서 시작점과 끝점이 아닌 점에서 끝점으로
    # 제일 큰 원판이 아닌 나머지를 옮기기
    hanoi(N-1, 6-start-end, end)

# 횟수: N-1개의 하노이탑 개수*2 + 1
# 직접 규칙 찾아보면 2**N - 1
print(2**N - 1)
# 1에서 시작해서 3에서 끝나게
hanoi(N, 1, 3)