import sys
from collections import deque

sys.stdin = open("input/BAEK_2164_카드_2.txt")
def input():
    return sys.stdin.readline().rstrip()

N = int(input())

cards = deque([card for card in range(1, N+1)])

while len(cards) > 1:
    cards.popleft()
    cards.rotate(-1)

print(cards[0])