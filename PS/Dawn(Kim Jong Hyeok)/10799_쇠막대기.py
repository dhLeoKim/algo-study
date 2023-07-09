import sys
def input():
    return sys.stdin.readline().rstrip()

razer = list(input())
stack = []
count = 0

for i in range(len(razer)):
    if razer[i] == '(':
        stack.append('(')
    else:
        if razer[i-1] == '(':
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1
print(count)