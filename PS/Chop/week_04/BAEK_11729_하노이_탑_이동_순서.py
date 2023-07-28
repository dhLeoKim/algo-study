from sys import stdin

stdin = open("input\BAEK_11729_하노이_탑_이동_순서.txt")

N = int(stdin.readline())

def h(n,f,b,t):
    if n==1:print(f,t)
    else:
        h(n-1,f,t,b)
        print(f,t)
        h(n-1,b,f,t)

print(2**N-1)

h(N,1,2,3)