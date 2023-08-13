N = int(input())
pinary = [0] * 91
pinary[1] = 1
pinary[2] = 1

for i in range(3, 91):
    pinary[i] = pinary[i-1] + pinary[i-2]

print(pinary[N])