import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

rods = input()
stack = []
temp = ''
ret = 0
for i in rods:
    if i == '(':
        stack.append(i)
        temp = '('
    elif i == ')':
        if temp == '(':
            stack.pop()
            ret += len(stack)
        elif temp == ')':
            ret += 1
            stack.pop()
        temp = ')'

print(ret)