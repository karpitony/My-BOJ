import sys
from collections import deque
input = sys.stdin.readline

# 큐이큐이
_deque = deque()
size = 0

for _ in range(0, int(input())):
    oper = input().strip()
    if oper == "pop":
        if size == 0:
            print(-1)
        else:
            print(_deque.popleft())
            size -= 1
            
    elif oper == "size":
        print(size)
    
    elif oper == "empty":
        print(1 if size == 0 else 0)
        
    elif oper == "front":
        if size == 0:
            print(-1)
        else:
            print(_deque[0])
            
    elif oper == "back":
        if size == 0:
            print(-1)
        else:
            print(_deque[-1])
            
    else:
        oper_, num = oper.split()
        _deque.append(num)
        size += 1