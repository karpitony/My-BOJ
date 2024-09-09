import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    num = 0
    for i in range(k):
       if num == 0:
           num = 1
       else:
           num = num*2 + 1
           
    print(num) 