import math
N = input()
chk = [0 for _ in range(10)]

for i in range(len(N)):
    chk[int(N[i])] += 1
# print(chk)

chk[6] = math.ceil((chk[6] + chk[9])/2)
chk[9] = 0
# print(chk)

print(max(chk))