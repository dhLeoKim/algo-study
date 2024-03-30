import sys
sys.stdin = open('input_20437.txt')
input = sys.stdin.readline

from collections import defaultdict

T = int(input())
for tc in range(T):
    W = input().strip()
    K = int(input())

    mn = 10005
    mx = 0

    alpha = defaultdict(list)
    for i in range(len(W)) :
        if W.count(W[i]) >= K :                     # W = abaaaba
            alpha[W[i]].append(i)	                # alpha = {'a': [0, 2, 3, 4, 6]}

    if alpha :
        for alpha_list in alpha.values() :	        # alpha_list = [0, 2, 3, 4, 6]
            for i in range(len(alpha_list)-K+1) :	# 3번 순회: (0~3), (2~4), (3~6)
                mn = min(mn, alpha_list[i+K-1] - alpha_list[i] + 1)
                mx = max(mx, alpha_list[i+K-1] - alpha_list[i] + 1)

        print(mn, mx)
    else :
        print(-1)