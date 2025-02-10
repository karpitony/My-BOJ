import sys
input = sys.stdin.readline

N = int(input())
set_ = set()
for _ in range(N):
    oper = input().strip()
    
    if oper == 'all':
        set_ = set(i for i in range(1, 21))
    elif oper == 'empty':
        set_ = set()
    else:
        # push
        oper, num = oper.split()
        num = int(num)
        if oper == 'add':
            set_.add(num)
        elif oper == 'remove':
            set_.discard(num)
        elif oper == 'check':
            print(1 if num in set_ else 0)
        elif oper == 'toggle':
            if num in set_:
                set_.discard(num)
            else:
                set_.add(num)
        