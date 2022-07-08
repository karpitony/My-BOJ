case = int(input())

for a in range(case):
    cnt, word = input().split()
    for b in word:
        print(b*int(cnt), end='')
    print()