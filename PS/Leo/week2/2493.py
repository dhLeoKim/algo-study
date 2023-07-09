import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

stack = [(0, 0)]
ret = []

for i in range(len(lst)):
    if lst[i] > stack[-1][0]:
        while stack and lst[i] > stack[-1][0]:
            stack.pop()
        if not stack:
            ret.append('0')
        else:
            ret.append(str(stack[-1][1]))
        stack.append((lst[i], i+1))
    elif lst[i] < stack[-1][0]:
        ret.append(str(stack[-1][1]))
        stack.append((lst[i], i+1))
        
print(' '.join(ret))

# 7
# 6 9 7 4 6 8 4