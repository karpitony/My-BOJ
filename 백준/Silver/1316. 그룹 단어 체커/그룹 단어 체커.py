import sys
input = sys.stdin.readline

cnt = 0
for _ in range(int(input())):
    word = input().strip()
    arr = []
    for i in range(len(word)):
        if word[i] not in arr:
            arr.append(word[i])
        
        elif arr[i-1] == word[i]:
            arr.append(word[i])
        
        elif arr[i-1] != word[i]:
            break

        # print(i, arr)
    else:
        cnt += 1
        
print(cnt)