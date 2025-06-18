import sys
input = sys.stdin.readline

N, M = map(int, input().split())

name_to_num = dict()
num_to_name = dict()

for i in range(1, N + 1):
    name = input().strip()
    name_to_num[name] = i
    num_to_name[str(i)] = name
    
for _ in range(M):
    userInput = input().strip()
    if userInput.isdigit():
        print(num_to_name[userInput])
    else:
        print(name_to_num[userInput])