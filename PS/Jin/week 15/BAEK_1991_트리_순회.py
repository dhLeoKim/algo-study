import sys

N = int(input())
ch1 = [0] * (N+1)
ch2 = [0] * (N+1)
# print(ord('A'))     # 65
for _ in range(N):
    p, c1, c2 = sys.stdin.readline().strip().split()
    if c1 != '.':
        ch1[ord(p) - 64] = ord(c1) - 64
    if c2 != '.':
        ch2[ord(p) - 64] = ord(c2) - 64

def preorder(n):
    global pre
    if n:
        pre += chr(n+64)
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n):
    global ino
    if n:
        inorder(ch1[n])
        ino += chr(n+64)
        inorder(ch2[n])

def postorder(n):
    global post
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        post += chr(n+64)

pre = ''
preorder(1)
print(pre)
ino = ''
inorder(1)
print(ino)
post = ''
postorder(1)
print(post)