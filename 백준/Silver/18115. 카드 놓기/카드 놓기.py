import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
commands = list(map(int, input().split()))
commands.reverse()
initial_cards = deque()

for card_num in range(1, N + 1):
    if commands[card_num - 1] == 1:
        initial_cards.appendleft(card_num)
    
    elif commands[card_num -1] == 2:
        initial_cards.insert(1, card_num)
    
    elif commands[card_num - 1] == 3:
        initial_cards.append(card_num)
 
for ic in initial_cards:
    print(ic, end=" ")