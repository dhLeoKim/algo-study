s = input()
stack = []
cnt = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')
    else:
        if s[i-1] == '(':
            cnt += len(stack) - 1
        else:
            cnt += 1
        stack.pop()
print(cnt)