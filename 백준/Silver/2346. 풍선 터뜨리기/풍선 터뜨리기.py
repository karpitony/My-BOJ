import sys
from collections import deque
from dataclasses import dataclass
input = sys.stdin.readline

@dataclass
class Ballown:
    index: int
    paper: int

N = int(input())
numbers = list(map(int, input().split()))
queue:deque[Ballown] = deque()

for i in range(N):
    queue.append(Ballown(i + 1, numbers[i]))

while queue:
    b:Ballown = queue.popleft()
    print(b.index, end=" ")
    if b.paper > 0:
        queue.rotate(-(b.paper - 1))
    else:
        queue.rotate(-b.paper)
    