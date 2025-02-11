import sys
input = sys.stdin.readline

arr = input().strip()
cnt = 0
numbers = []

for a in arr:
    a = int(a)
    if a == 9:
        a = 6
        
    if a in numbers:
        numbers.remove(a)
        
    else:
        cnt += 1
        numbers.extend(i for i in range(0, a))
        numbers.extend(i for i in range(a+1, 9))
        numbers.append(6)
        
print(cnt)
        