import sys
input = sys.stdin.readline

num = int(input())
arrays = [0 for _ in range(num + 1)]
for i in range(1, num):
    if arrays[i] != 0:
        break
    
    if num % i == 0:
        arrays[i] = 1
        arrays[num // i] = 1

sigma = 0
for i in range(1, num + 1):
    if arrays[i] != 0:
        sigma += i
        
print(sigma)