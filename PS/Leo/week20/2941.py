import sys
sys.stdin = open('input_2941.txt')
input = sys.stdin.readline

from collections import defaultdict

word = input().strip()

croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for alpha in croatian:
    word = word.replace(alpha, 'a')

print(len(word))