import sys
input = sys.stdin.readline

stack = list()
K = int(input())
arr = list(int(input()) for _ in range(K))
answ = list()

idx = 0
num = 1

while (True):
    if (idx >= K):
        break
    
    while num <= arr[idx]:
        stack.append(num)
        answ.append("+")
        num += 1
    
    if (stack.pop() == arr[idx]):
        answ.append("-")
        idx += 1
    else:
        print("NO")
        exit(0)
    
for a in answ:
    print(a)