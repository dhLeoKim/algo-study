N = int(input())
tower = list(map(int, input().split()))
answer = []
stack = []

for i in range(N):
    # i번째 tower값보다 작은 값을 pop 시키기 위해 while문 이용
    while stack:
        if stack[-1][1] >= tower[i]:
            answer.append(stack[-1][0])
            break
        else:
            stack.pop()
            # 여기에 stack.append([i+1, tower[i]])를 사용하면
            # tower보다 작은 모든 값을 pop 시킬 수 없음
    # tower값이 제일 큰 경우 0을 답으로 입력해야 하기 때문에
    # if not stack이 while문 아래에 있어야 함
    if not stack:
        answer.append(0)
    stack.append([i+1, tower[i]])

print(*answer)