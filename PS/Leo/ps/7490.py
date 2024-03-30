import sys
sys.stdin = open('input_7490.txt')
input = sys.stdin.readline

def dfs(depth, temp):
    if depth == N:
        ret = temp.replace(' ', '')
        if eval(ret) == 0:
            print(temp)
        return
    
    dfs(depth+1, temp+' '+str(depth+1))
    dfs(depth+1, temp+'+'+str(depth+1))
    dfs(depth+1, temp+'-'+str(depth+1))


T = int(input())
for _ in range(T):
    N = int(input())

    dfs(1, '1')    

    print()