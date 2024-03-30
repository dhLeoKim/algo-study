import sys
sys.stdin = open('input_9935.txt')
input = sys.stdin.readline

string = list(input().strip())
bomb = list(input().strip())

stack = []
for char in string:
    stack.append(char)
    if stack[len(stack)-len(bomb):len(stack)] == bomb:
        for _ in range(len(bomb)):
            stack.pop()

if stack:
    print(*stack, sep='')
else:
    print('FRULA')