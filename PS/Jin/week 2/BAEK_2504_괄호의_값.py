# 분배법칙과 유사한 방식
bracket = input()
stack = []
answer = 0
temp = 1

for i in range(len(bracket)):
    if bracket[i] == '(':
        stack.append('(')
        temp *= 2
    elif bracket[i] == '[':
        stack.append('[')
        temp *= 3
    elif bracket[i] == ')':
        if not stack or stack[-1] != '(':
            answer = 0
            break
        if bracket[i-1] == '(':
            answer += temp
        # stack[-1]값이 '('이고 bracket[i-1]값이 '('가 아닌 경우도
        # stack.pop()과 temp //= 2를 해주어야 함
        stack.pop()
        temp //= 2
    else:
        if not stack or stack[-1] != '[':
            answer = 0
            break
        if bracket[i-1] == '[':
            answer += temp
        stack.pop()
        temp //= 3

if stack:
    print(0)
else:
    print(answer)