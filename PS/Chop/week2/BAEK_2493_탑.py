import sys

sys.stdin = open("input/BAEK_2493_탑.txt")
N = int(sys.stdin.readline().rstrip())
towers = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

stack = [(0, 0)]  # 레이저를 수신할 가능성이 있는 탑들, 원소는 (index, height)

def receiving_tower(i):
    global stack

    if towers[i] >= stack[0][1]:  # 현재까지 가장 높은 탑보다 크거나 같을 때
        stack = [(i, towers[i])]  # stack 전체 지우고 현재 타워로 갱신
        return "0"
    
    while stack:                            # stack의 가장 작은 탑부터 비교
        if towers[i] >= stack[-1][1]:       # stack의 가장 작은 탑보다 크거나 같을 때, stack의 가장 작은 탑 제거
            stack.pop()                     
        else:                               # stack의 가장 작은 탑보다 작을 때, stack에 현재 타워 추가
            stack.append((i, towers[i]))    
            return str(stack[-2][0])        # stack의 가장 작은 탑의 index 반환

res = map(receiving_tower, range(1, len(towers)))
print(" ".join(res))