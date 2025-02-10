import sys
input = sys.stdin.readline

N = int(input())
queue = []
for _ in range(N):
    oper = input().strip()
    
    if oper == 'size':
        print(len(queue))
    elif oper == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif oper == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif oper == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif oper == 'pop':
            if queue:
                print(queue.pop(0))
            else:
                print(-1)
    else:
        # push
        oper, num = oper.split()
        num = int(num)
        queue.append(num)
        