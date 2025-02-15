import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
_deque = deque(range(1, N + 1))
ans = list()

j = 1
while _deque: 
    if j % K == 0:
        ans.append(int(_deque.popleft()))
    else:
        _deque.rotate(-1)
    j += 1
    
print("<" + ", ".join(map(str, ans)) + ">")