import sys
sys.stdin = open('input_1991.txt')
input = sys.stdin.readline

def preorder(now):
    print(chr(now+65), end='')
    if lc[now] != 0: preorder(lc[now])
    if rc[now] != 0: preorder(rc[now])


def inorder(now):
    if lc[now] != 0: inorder(lc[now])
    print(chr(now+65), end='')
    if rc[now] != 0: inorder(rc[now])


def postorder(now):
    if lc[now] != 0: postorder(lc[now])
    if rc[now] != 0: postorder(rc[now])
    print(chr(now+65), end='')


N = int(input())
lc = [0]*(N)
rc = [0]*(N)
for _ in range(N):
    V, L, R = input().split()
    v = ord(V)-65
    if L.isalpha():
        lc[v] = ord(L)-65
    if R.isalpha():
        rc[v] = ord(R)-65

preorder(0)
print()

inorder(0)
print()

postorder(0)
print()